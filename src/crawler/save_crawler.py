#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import os
import warnings

from src.collector.bs4 import Bs4Collector
from src.util import file_manager

warnings.filterwarnings(action='ignore')


class SaveCrawler:
    """웹 페이지를 저장하면서 크롤링을 한다."""

    def __init__(self, q):
        pass

    @staticmethod
    def get_md5(raw_text):
        """MD5 값을 가져온다."""
        return hashlib.md5(raw_text.encode("utf-8")).hexdigest()

    def save_file(self, url, text, dest_path):
        """파일로 저장한다.

        :param text: 내용
        :param dest_path: 저장 경로
        :return: {boolean} 저장 성공 또는 실패
        """

        # 디렉토리가 없는 경우, 디렉토리를 만든다.
        _base_dir, filename = os.path.split(dest_path)
        if not os.path.exists(_base_dir):
            os.makedirs(_base_dir)

        # 파일 종류에 따라 저장한다.
        # 1. 텍스트 파일 저장
        if ".css" in url:
            file_manager.create_css_file(dest_path, text, overwrite=True)
        elif ".js" in url:
            file_manager.create_js_file(dest_path, text, overwrite=True)
        else:
            file_manager.create_html_file(dest_path, text, overwrite=True)

        # TODO 2. 이미지인 경우

    def crawler(self, url, save_path):
        """crawling & save files

        :param url: 크롤링을 할 URL 주소
        :param save_path: 크롤링을 한 파일을 저장할 경로
        :return: {list} 크롤링한 페이지 내부에 있는 모든 url 리스트
        """
        # 페이지를 가져온다.
        text = Bs4Collector.get_page(url)

        # 파일로 저장한다.
        md5 = self.get_md5(url)
        self.save_file(url, text, os.path.join(save_path, md5))

        # 내부 URL 을 반환한다.
        bs = Bs4Collector()
        url_list = bs.get_url_by_page(url, text)
        return url_list
