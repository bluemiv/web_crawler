#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

import bs4
import requests


class Bs4Collector:
    def __init__(self):
        pass

    @staticmethod
    def _get_page(url, verify=False, retry=5):
        """웹 페이지를 가져온다."""
        response = requests.get(url=url, verify=verify)

        for _ in range(retry):
            if response.status_code == 200:
                return response.text
            else:
                print("Fail to get page. status code: {}, url: {}".format(response.status_code, url))

        return ""

    def get_url_by_page(self, url):
        """웹 페이지 내부의 모든 url 을 가져온다."""
        text = self._get_page(url)
        url_set = set()

        if text:
            search = re.search("(^https?://.+/)", url)
            if search:
                base_url = search.group()
            else:
                search = re.search("(^https?://.+)", url)
                base_url = search.group() if search else ""

            if base_url:
                base_url = base_url[:-1] if base_url.endswith("/") else base_url

            soup = bs4.BeautifulSoup(text, 'html.parser')
            for a_tag in soup.find_all("a", href=True):
                href_url = a_tag["href"]
                if re.match(r"^https?://.+", href_url):
                    url_set.add(href_url)
                else:
                    if base_url:
                        relative_url = base_url + ("" if href_url.startswith("/") else "/") + href_url
                        url_set.add(relative_url)

        return list(url_set)
