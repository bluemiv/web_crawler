#!/usr/bin/python3
# -*- coding: utf-8 -*-


class KeywordCrawler:
    """키워드를 가지고 크롤링을 한다."""

    def __init__(self, keyword_list):
        self._keyword_list = keyword_list

    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, keyword_list):
        self.keyword_list = keyword_list if isinstance(list, keyword_list) else list()

    @staticmethod
    def get_keyword_count(keyword, text):
        """웹 페이지 내부의 키워드 카운트를 가져온다."""
        assert isinstance(str, text) and isinstance(str, keyword), "Invalid type of arguments. keyword/text: {}".format(
            map(type, [keyword, text])
        )
        return text.count(keyword)
