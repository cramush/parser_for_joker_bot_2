import requests
import lxml.html
from filling_db import filling_data
from time import sleep

URL = "https://baneks.ru/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"}


def get_urls_list_and_tag():
    request = requests.get(URL, headers=HEADERS)
    tree = lxml.html.document_fromstring(request.text)
    tag = tree.xpath('//head/title/text()')
    tag = "".join(tag)

    urls_list = []
    for link in range(1, 1142+1):
        url = URL + str(link)
        urls_list.append(url)

    for url in urls_list:
        get_jokes(tag, url)
        sleep(5)


def get_jokes(tag, url):
    request = requests.get(url, headers=HEADERS)
    tree = lxml.html.document_fromstring(request.text)
    joke = tree.xpath('//section[@class="anek-view"]/article/p/text()')
    joke = "".join(joke)

    filling_data(tag, joke)


if __name__ == '__main__':
    get_urls_list_and_tag()
