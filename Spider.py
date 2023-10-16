# web scrapper official tool
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

print("SSSSSS   SSSSSS   SSSSSS   SSSSSSS   SSSSSS   SSSSSSSS  ")
print("SS       SS  SS     SS       S  SS   SS       SS    SS")
print("SSSSSS   SSSSSS     SS       S  SS   SSSSSS   SS  SSS ")
print("    SS   SS         SS       S  SS   SS       SS    SS")
print("SSSSSS   SS       SSSSSS   SSSSSSS   SSSSSS   SS    SS")
print('\n')
print("By Scorpion")

visited_urls = set()


def web_scaper(url, keyword):
    try:
        response = requests.get(url)

    except:
        print(f"request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    web_scaper(url, keyword)
                else:
                    pass

        print(urls)


url = input("Enter Url: ")
keyword = input("Enter Key word you would like obtain links related to: ")

web_scaper(url, keyword)


