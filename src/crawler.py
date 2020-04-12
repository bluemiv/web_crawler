#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import os
import queue
import threading
import time
import warnings

from src.collector.bs4 import Bs4Collector
from src.util import file_manager

warnings.filterwarnings(action='ignore')


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


if __name__ == "__main__":
    save_path = os.path.abspath("./collected_page")

    thread_count = 4

    base_url = "https://www.naver.com"
    q = queue.Queue()
    q.put(base_url)

    thread_list = list()
    for _ in range(thread_count):
        thread = threading.Thread(target=crawler, args=(q, save_path), name="thread{}".format(_))
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()
