import ssl
import urllib.request

url = r"https://www.naver.com" # seed url
context = ssl._create_unverified_context() # SSL 처리
html = urllib.request.urlopen(url, context=context)

print(html.read())
