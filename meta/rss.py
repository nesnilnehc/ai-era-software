"""Deterministic RSS from the catalog and substantive question revisions."""
from datetime import datetime, timezone
from email.utils import format_datetime
import hashlib
import json
import xml.etree.ElementTree as ET

FEED_URL = 'https://raw.githubusercontent.com/nesnilnehc/ai-era-software/main/feed.xml'
SITE_URL = 'https://ai-era-software.nesnilnehc.top/'
ATOM = 'http://www.w3.org/2005/Atom'
ET.register_namespace('atom', ATOM)


def date_value(value):
    # Month precision uses its first day solely for RSS date encoding.
    return datetime.fromisoformat(value + '-01' if len(value) == 7 else value).replace(tzinfo=timezone.utc)


def question_revision(question):
    # Rechecking a URL or editing the audit log alone is not a content revision.
    payload = {key: value for key, value in question.items() if key not in ('updated', 'history', 'sources')}
    payload['sources'] = [{key: value for key, value in source.items() if key != 'checked'} for source in question['sources']]
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:24]


def render_feed(items, data):
    entries = []
    for item in items:
        description = ('原文首发日期：%s%s。原文最后更新：%s。历史材料缺少本项目收录时间；'
                       'RSS pubDate 使用原文首发日期，不代表本项目新增时间。\n%s\n收录理由：%s'
                       % (item.first, '（仅精确到月；RSS 以月初表示）' if len(item.first) == 7 else '', item.updated, item.summary or '摘要待核实，请阅读原文。', item.rationale))
        guid = 'urn:ai-era-software:material:' + hashlib.sha256(item.url.encode('utf-8')).hexdigest()
        entries.append((date_value(item.first), guid, '[资料] ' + item.title, item.url, description, item.topics))
    for question in data['questions']:
        guid = 'urn:ai-era-software:question:%s:%s' % (question['id'], question_revision(question))
        description = ('问题实质修订日期：%s（仅精确到日；RSS 时间部分统一用 UTC 00:00 表示）。'
                       '状态：%s；类型：%s。待研究问题，不代表已验证结论。\n研究价值：%s\n已知：%s\n未知：%s\n候选：%s'
                       % (question['updated'], question['status'], question['kind'], question['value'], question['known'], question['unknown'], '；'.join(option['id'] + ' ' + option['content'] for option in question['options']) or '尚未形成，见下一步查证'))
        entries.append((date_value(question['updated']), guid, '[问题] ' + question['title'], SITE_URL + '#' + question['id'], description, question['topics']))
    entries.sort(key=lambda entry: (entry[0], entry[1]), reverse=True)
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    def child(parent, name, content):
        ET.SubElement(parent, name).text = content
    child(channel, 'title', 'AI 重构软件 · 资料与问题探索')
    child(channel, 'link', SITE_URL)
    child(channel, 'description', '一手资料目录与问题实质修订。历史资料日期是原文首发日期，非本项目收录时间；问题是待研究内容。')
    child(channel, 'language', 'zh-cn')
    child(channel, 'ttl', '60')
    ET.SubElement(channel, '{%s}link' % ATOM, href=FEED_URL, rel='self', type='application/rss+xml')
    if entries:
        child(channel, 'lastBuildDate', format_datetime(entries[0][0], usegmt=True))
    for published, guid, title, url, description, topics in entries:
        element = ET.SubElement(channel, 'item')
        child(element, 'title', title)
        child(element, 'link', url)
        ET.SubElement(element, 'guid', isPermaLink='false').text = guid
        child(element, 'pubDate', format_datetime(published, usegmt=True))
        child(element, 'description', description)
        for topic in topics:
            child(element, 'category', topic)
    ET.indent(rss, space='  ')
    return '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(rss, encoding='unicode') + '\n'
