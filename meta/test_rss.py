import copy
from datetime import timezone
from email.utils import parsedate_to_datetime
import unittest
import xml.etree.ElementTree as ET
from catalog import Item, ITEMS
from questions import load_questions
from rss import FEED_URL, question_revision, render_feed
import build

class RSSFeedTests(unittest.TestCase):
    def setUp(self):
        self.item=Item(*ITEMS[0]); self.data=load_questions()
    def test_parse_escape_and_source_date_semantics(self):
        item=self.item._replace(title='A & B <test>', summary='Text & <XML>')
        root=ET.fromstring(render_feed([item],self.data))
        material=next(i for i in root.findall('channel/item') if i.findtext('title').startswith('[资料]'))
        self.assertEqual(material.findtext('title'),'[资料] A & B <test>')
        self.assertIn('Text & <XML>',material.findtext('description'))
        self.assertEqual(material.findtext('link'),item.url)
        self.assertIn('不代表本项目新增时间',material.findtext('description'))
    def test_guid_stability_and_substantive_question_revision(self):
        q=self.data['questions'][0]; original=question_revision(q); altered=copy.deepcopy(q)
        altered['updated']='2026-10-23';altered['history'].append({'date':'2026-10-23','reason':'核读无变化'});altered['sources'][0]['checked']='2026-10-23'
        self.assertEqual(question_revision(altered),original)
        altered['options'][0]['content']+='新增具体条件'
        self.assertNotEqual(question_revision(altered),original)
    def test_no_change_build_and_date_order(self):
        first=render_feed([self.item],self.data)
        self.assertEqual(first,render_feed([self.item],self.data))
        root=ET.fromstring(first);dates=[parsedate_to_datetime(i.findtext('pubDate')) for i in root.findall('channel/item')]
        self.assertEqual(dates,sorted(dates,reverse=True))
        self.assertEqual(parsedate_to_datetime(root.findtext('channel/lastBuildDate')),max(dates))
    def test_all_guids_unique_and_question_links_open_details(self):
        root=ET.fromstring(render_feed([Item(*i) for i in ITEMS],self.data));entries=root.findall('channel/item')
        guids=[i.findtext('guid') for i in entries];self.assertEqual(len(guids),len(set(guids)))
        question=next(i for i in entries if i.findtext('title').startswith('[问题]'))
        self.assertTrue(question.findtext('link').endswith('#Q-0001'))
    def test_build_includes_feed_and_exact_self_url(self):
        _, outputs=build.render_outputs();root=ET.fromstring(outputs['feed.xml'])
        self.assertEqual(root.find('channel/{http://www.w3.org/2005/Atom}link').get('href'),FEED_URL)

    def test_month_precision_and_material_guid_survives_summary_edit(self):
        item=self.item._replace(first="2025-03")
        root=ET.fromstring(render_feed([item],self.data))
        material=next(i for i in root.findall('channel/item') if i.findtext('title').startswith('[资料]'))
        self.assertEqual(parsedate_to_datetime(material.findtext('pubDate')).day,1)
        self.assertIn('仅精确到月',material.findtext('description'))
        changed=ET.fromstring(render_feed([item._replace(summary='Corrected summary')],self.data))
        other=next(i for i in changed.findall('channel/item') if i.findtext('title').startswith('[资料]'))
        self.assertEqual(material.findtext('guid'),other.findtext('guid'))
