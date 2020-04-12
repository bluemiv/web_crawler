#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import queue
import time


class SaveCrawler:
    """웹 페이지를 저장하면서 크롤링을 한다."""

    def __init__(self, q):
        pass


def crawler(_q, _save_path):
    """crawling"""
    print("Parent:", os.getppid(), "/ Child:", os.getpid())
    assert isinstance(_q, queue.Queue), "Invalid data structure. {}".format(type(_q))

    if _q.empty():
        time.sleep(5)

    while not _q.empty():
        _url = _q.get()
        print("[{}]Start crawling {}".format(threading.Thread().name, _url))

        text = Bs4Collector.get_page(_url)
        md5 = hashlib.md5(_url.encode("utf-8")).hexdigest()
        if ".css" in _url:
            css_path = os.path.join(_save_path, "css")
            if not os.path.exists(css_path):
                os.makedirs(css_path)
            file_manager.create_css_file(os.path.join(css_path, md5), text, overwrite=True)
        elif ".js" in _url:
            js_path = os.path.join(_save_path, "js")
            if not os.path.exists(js_path):
                os.makedirs(js_path)
            file_manager.create_js_file(os.path.join(js_path, md5), text, overwrite=True)
        else:
            html_path = os.path.join(_save_path, "html")
            if not os.path.exists(html_path):
                os.makedirs(html_path)
            file_manager.create_html_file(os.path.join(html_path, md5), text, overwrite=True)

        bs = Bs4Collector()
        url_list = bs.get_url_by_page(_url, text)
        for new_url in url_list:
            q.put(new_url)

    print("The end crawler")
