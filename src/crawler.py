#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import queue

if __name__ == "__main__":
    save_path = os.path.abspath("./collected_page")

    thread_count = 4

    base_url = "https://www.naver.com"
    q = queue.Queue()
    q.put(base_url)

    thread_list = list()
    # for _ in range(thread_count):
    #     thread = threading.Thread(target=crawler, args=(q, save_path), name="thread{}".format(_))
    #     thread.start()
    #     thread_list.append(thread)
    #
    # for thread in thread_list:
    #     thread.join()
