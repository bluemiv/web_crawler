import re
import ssl
import queue
import urllib.request

import bs4

class cCrawling :
    def __init__(self, url):
        p = re.compile(r"^(http)(s)?://[a-zA-Z0-9]+")
        m = p.match(url)
        if not m :
            raise RuntimeError("Invalid value for seed url. <DEBUG - url : {}".format(url))

        self.url_queue = queue.Queue()
        self.url_queue.put(url)

    def ReadUrl(self, url):
        """
        URL을 읽어오는 메소드
        :param url:읽고싶은 url
        :return: html conext
        """
        context = ssl._create_unverified_context()
        html_context = ""
        try :
            html = urllib.request.urlopen(url, context=context)
            html_context = bs4.BeautifulSoup(html, "html.parser")
        except Exception as e:
            print("Error :", url, "err_msg :", str(e))

        return html_context

    def GetUrlListFromATag(self, context):
        """
        BS4를 이용하여 a tag들의 모든 url을 가져옴
        :param context: html context
        :return: url list
        """
        url_list = []
        try:
            a_tag_list = context.findAll("a")

            p = re.compile(r"^(http)(s)?://")

            url_list = [ a_tag.get("href") for a_tag in a_tag_list if p.match(a_tag.get("href")) ]
        except :
            print(url_list)

        return list(set(url_list)) # 중복 제거

    def _InsertQueue(self, url_list):
        """
        URL queue에 담음
        :param url_list: URL들이 담겨있는 리스트
        :return: N/A
        """
        for url in url_list :
            self.url_queue.put(url)

        # print(self.url_queue)

    def run(self):
        cnt = 0
        while not self.url_queue.empty():
            seed_url = self.url_queue.get()
            print(seed_url, self.url_queue.qsize(), "현재 수집 URL :", cnt+1)
            # print(seed_url, "현재 수집 URL :", cnt + 1)
            context = self.ReadUrl(seed_url)
            url_list = self.GetUrlListFromATag(context)
            self._InsertQueue(url_list)
            # print(self.url_queue.get())
            cnt += 1
            # if cnt >= 1000:
            #     break

if __name__ == "__main__" :
    # seed_url = r"https://www.naver.com"
    # seed_url = r"https://www.daum.net"
    # seed_url = r"http://www.ssu.ac.kr/web/kor/home_visual"
    # seed_url = r"https://comic.naver.com/webtoon/weekday.nhn"
    seed_url = r"https://comic.naver.com/webtoon/list.nhn?titleId=697656&weekday=sun"

    c = cCrawling(seed_url)
    c.run()
