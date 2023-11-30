from requests_html import AsyncHTMLSession
from requests_html import HTMLSession
import asyncio
import time
asession = AsyncHTMLSession()


def get_manga_page(n):
    url_string = "https://bilingualmanga.org/manga/636f632fbd9f0ab40a280919?lang=jp&chen=0&chjp=0&enp=0&jpp={}#img_store".format(n)


    r = s.get(url_string)
    r.html.render(sleep=2, timeout=10000)

    element = r.html.find('#img_store', first=True)
    print(n+1)
    if(element.text != None):
        return element.text
    return 'empty'

def main(limit):
    for n in range(limit):
        print(get_manga_page(n))

s = HTMLSession()
main(205)


# for n in range(205):
#     url_string = "https://bilingualmanga.org/manga/636f632fbd9f0ab40a280919?lang=jp&chen=0&chjp=0&enp=0&jpp={}#img_store".format(n)
#
#     session = HTMLSession()
#     response = session.get(url_string)
#     response.html.render(sleep=2, timeout=10000)
#
#     element = response.html.find('#img_store', first=True)
#     print(n+1)
#     if(element.text != None):
#         print(element.text)
#

# from requests_html import AsyncHTMLSession
# asession = AsyncHTMLSession()
#
# async def get_pythonorg():
#     r = await asession.get('https://python.org/')
#
# async def get_reddit():
#     r = await asession.get('https://reddit.com/')
#
# async def get_google():
#    r = await asession.get('https://google.com/')
#
# session.run(get_pythonorg, get_reddit, get_google)