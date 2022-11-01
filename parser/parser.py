from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS

URL = "https://doramy.club/"

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("div", class_="post-home")
    dorama = []
    for item in items:
        # datetime = item.find("time").getText()
        dorama.append({
            "title": item.find('div', class_="post-home").find('a').getText()
        })
    pprint(dorama)

html = get_html(URL)
get_html(html.text)

    #         "link": item.find('div', class_="post-home").find('a').getText('href'),
    #         "time": datetime[:5],
    #         "day": datetime[8:].split(", ")[0],
    #         "year": datetime[8:].split(", ")[1]
    #     })
#     # return dorama
#
#
# def parser():
#     html = get_html(URL)
#     if html.status_code == 200:
#         dorama = []
#         for i in range(1, 3):
#             html = get_html(f'{URL}page/{i}/')
#             current_page = get_data(html.text)
#             dorama.extend(current_page)
#         return dorama
#     else:
#         pass

#
# if __name__ == '__main__':
#     # print(0)
#     # print(html.text)
#     pprint(parser())
