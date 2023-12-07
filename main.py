import asyncio
import aiohttp


from requests_html import AsyncHTMLSession
from requests_html import HTMLSession
import asyncio
import time

def get_manga_page(n):
    url_string = "https://bilingualmanga.org/manga/6408ace1df8a4333a0c37e7a?lang=jp&chen=0&chjp=0&enp=0&jpp={}#img_store".format(n)


    r = s.get(url_string)
    r.html.render(sleep=3, timeout=10000)

    element = r.html.find('.ocrtext')
    print(n, end='\n\n')
    if(element is not None):
        return element
    return 'whaaat'

def main(limit):
    l = list()
    for n in range(limit):
        l = get_manga_page(n)
        for i in l:
            print(i.text)
            print()

s = HTMLSession()
main(205)
