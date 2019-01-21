# Copyright © Taehong Kim, All rights reserved.
# -*- coding: utf-8 -*-
# Pytho 3.7

import os
import re
import ssl
import time
import queue
import threading
import urllib.parse
import urllib.request

import bs4

class cMyCrawler(threading.Thread):

    def __init__(self, thread_id, url_queue):
        threading.Thread.__init__(self)
        self.ssl_context = ssl._create_unverified_context()  # SSL 처리
        self.thread_id = thread_id # thread 구분하기 위한 id 값
        self.url_queue = url_queue # url를 담고 있는 queue


    # file 생성
    def CreateFile(self, url, context):
        u = urllib.parse.urlparse(url)
        dir_list = [u.scheme, u.netloc, u.path]
        filename = os.path.join(r"/Users/taehongkim/Desktop/html_files", "/".join([ dir.strip() for dir in dir_list if dir != "/" and dir ]))
        if not os.path.exists(filename) :
            f_path, f_name = os.path.split(filename)
            os.makedirs(f_path, exist_ok=True)
            with open(filename + ".html", "w", encoding="utf-8") as f:
                f.write(context)

    # 실행
    def run(self):
        retry = 0
        MAX_RETRY_CNT = 3
        while True :
            if retry >= MAX_RETRY_CNT :
                # retry를 하면서, 다른 쓰레드의 결과를 기다림
                break

            if self.url_queue.empty() :
                time.sleep(1) # 너무 빨라서 약간의 1초 딜레이
                retry += 1
            else :
                url = self.url_queue.get() # queue에서 url을 가져옴
                try :
                    # html을 읽어옴
                    html = urllib.request.urlopen(url, context=self.ssl_context)
                    bs_obj = bs4.BeautifulSoup(html, "html.parser")

                    # 파일 생성
                    self.CreateFile(url, str(bs_obj.contents))
                except Exception as e:
                    # Encoding 에러 등등
                    print(str(e))

                try :
                    a_tags = bs_obj.findAll("a")

                    p = re.compile(r"^(http)(s)?://") # http 또는 https로 시작하는 url 가져옴

                    for a_tag in a_tags:
                        tmp_url = a_tag.get("href") # a 태그의 href에 들어있는 url 값을 가져옴
                        m = p.match(tmp_url)
                        if m :
                            self.url_queue.put(tmp_url) # 가져온 url를 queue에 담아둠

                            # 해당 디렉토리에 결과 로그 파일 생성
                            with open("log.txt", "a") as f :
                                log_text = "thread-{} : {}\n".format(self.thread_id, tmp_url)
                                f.write(log_text)
                                print(log_text) # for console
                except Exception as e:
                    # Encoding 에러 등 기타 에러
                    print(str(e))


if __name__ == "__main__":
    print("Start Crawling")

    seed_url = r"https://www.naver.com"

    url_queue = queue.Queue()
    url_queue.put(seed_url)
    total_cnt = 0

    # 쓰레드 생성
    thread_cnt = 4
    thread_list = []
    for thread_id in range(thread_cnt):
        crawler = cMyCrawler(thread_id, url_queue)
        thread_list.append(crawler)

    # 시작
    for thread in thread_list :
        thread.start()

    # 끝나기를 기다림
    for thread in thread_list:
        thread.join()

    print("End.")