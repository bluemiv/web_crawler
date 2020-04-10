#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest

from src.collector.bs4 import Bs4Collector


class Bs4UnitTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.google_url = "https://www.google.com"
        cls.google_url2 = "https://www.google.com/"
        cls.google_url3 = "https://www.google.com/advanced_search?hl=ko&authuser=0"
        cls.bs = Bs4Collector()

    def test_get_page(self):
        """_get_page() Test"""
        text = self.bs._get_page(self.google_url, verify=False, retry=1)
        self.assertTrue(text)

    def test_get_url_by_page(self):
        """get_url_by_page() Test"""
        urls = self.bs.get_url_by_page(self.google_url)
        urls2 = self.bs.get_url_by_page(self.google_url)
        urls3 = self.bs.get_url_by_page(self.google_url)
        print(urls, urls2, urls3)


if __name__ == "__main__":
    unittest.main()
