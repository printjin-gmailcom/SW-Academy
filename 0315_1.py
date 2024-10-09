# CSSOM -> CSS Rules -> Sselector (*)
# ; 지칭, 구조, 관계
# + pesudo select
# 태그이름, #아이디, .클래스, .클래스.클래스, 태그이름#아이디, #아이디.클래스
# 띄어쓰기는 자손을 의미, .클래스.클래스 와 .클래스 .클래스 이 다른 의미
# 자손, 자식 >
# 바로 다음 형제 +, 다음 형제 노드 들 ~
# span + a    <p>    <spna></spna><a></a><a></a><a></a><a></a><a></a><a></a><?>    </p>
# :has, :is
# a:is(.A)
#    < a class="A"> < a class="B">
# :nth-child 같은 부모를 공유하는 자식들의 순번, ;nth-of-tpye 같은 종류의 태그 중 순번

# crawler -> crawling
# link를 따라 다니면서 웹페이지에 무슨 내용이 있었는지 수집 (indexing, scraping) + 다음 link 찾아서 또 따라다니는 *
# Tree - BFS, DFS ~ link를 어떻게 찾나 ~ 정규화 ~ 다음에 방문할 링크 ~ FORCUSED CRAWLING ~ scraping + DB ~ 우선순위 ~ citation(href;linking) ~ pagerank

import requests
from requests.exceptions import HTTPError
from requests.compat import urljoin
from time import sleep
from bs4 import BeautifulSoup
import re

def download(url, params={}, data={}, headers={}, method='GET', retries=3):

    resp = requests.request(method, url, params=params, data=data, headers=headers)

    try:
        resp.raise_for_status()
    except HTTPError as e:
        if retries > 0 and 499 < response.status_code :
            print('Retrying...')
            sleep(5)
            return download(url, params, data, headers, method, retries - 1)
        else:
            print(e.response.status_code)
            print(e.request.headers)
            print(e.response.headers)
            return None


    return resp

URLs = ['https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%88%98%EC%A7%80']
Visited = []

while URLs:
    url = URLs.pop(-1) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    Visited.append(url)

    resp = download(url, headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    if resp is None:
        continue

    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        for link in dom.select('''a[href], frame[src], iframe[src], img[src],
        audio[src], video[src], style[src], link[src]'''):
            newURL = link.attrs['href'] if link.has_attr('href') else link.attrs['src']

            if not re.match(r'#|javascript|mailto', newURL):
                normalizedURL = urljoin(url, newURL)
                if normalizedURL not in Visited and \
                   normalizedURL not in URLs:
                    URLs.append(normalizedURL)

    print(len(URLs), len(Visited))

URLs = [ ]
Visited = []
Skipped = []
depth = 3

# Forcused Crawling
# Depth 제한
# Domain 제한
# HTML Tags 제한



URLs.append({'link':'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=수지', 'depth':0})

while URLs:
    url = URLs.pop(-1) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    if url['depth'] > depth:
        Skipped.append(url['link'])
        continue

    resp = download(url['link'], headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    Visited.append(url['link'])

    if resp is None:
        continue

    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        for link in dom.select('''a[href], frame[src], iframe[src], img[src],
        audio[src], video[src], style[src], link[src]'''):
            newURL = link.attrs['href'] if link.has_attr('href') else link.attrs['src']

            if not re.match(r'#|javascript|mailto', newURL):
                normalizedURL = urljoin(url['link'], newURL)
                if normalizedURL not in Visited and \
                   normalizedURL not in URLs and \
                   normalizedURL not in Skipped :
                    URLs.append({'link':normalizedURL, 'depth':url['depth']+1})

    print(len(URLs), len(Visited))

from urllib.parse import urlparse

URLs = [ ]
Visited = []
Skipped = []
depth = 3
optin = ['v.daum.net']
optout = []



# Forcused Crawling
# Depth 제한
# Domain 제한
# HTML Tags 제한



URLs.append({'link':'https://search.daum.net/search?DA=YZR&orgq=tnwl&q=수지', 'depth':0})

while URLs:
    url = URLs.pop(-1) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    if url['depth'] > depth:
        Skipped.append(url['link'])
        continue

    resp = download(url['link'], headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    Visited.append(url['link'])

    if resp is None:
        continue

    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        for link in dom.select('''a[href], frame[src], iframe[src], img[src],
        audio[src], video[src], style[src], link[src]'''):
            newURL = link.attrs['href'] if link.has_attr('href') else link.attrs['src']

            if not re.match(r'#|javascript|mailto', newURL):
                normalizedURL = urljoin(url['link'], newURL)
                if urlparse(normalizedURL).netloc not in optin:
                    continue
                if normalizedURL not in Visited and \
                   normalizedURL not in URLs and \
                   normalizedURL not in Skipped :
                    URLs.append({'link':normalizedURL, 'depth':url['depth']+1})

    print(len(URLs), len(Visited))

from urllib.parse import urlparse

URLs = [ ]
Visited = []
Skipped = []
depth = 3
optin = ['v.daum.net']
optout = []



# Forcused Crawling
# Depth 제한
# Domain 제한
# HTML Tags 제한



URLs.append({'link':'https://search.daum.net/search?DA=YZR&orgq=tnwl&q=수지', 'depth':0})

while URLs:
    url = URLs.pop(-1) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    if url['depth'] > depth:
        Skipped.append(url['link'])
        continue

    resp = download(url['link'], headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    Visited.append(url['link'])

    if resp is None:
        continue

    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        for link in dom.select('''a[href], frame[src], iframe[src], img[src],
        audio[src], video[src], style[src], link[src]'''):
            newURL = link.attrs['href'] if link.has_attr('href') else link.attrs['src']

            if not re.match(r'#|javascript|mailto', newURL):
                normalizedURL = urljoin(url['link'], newURL)
                if urlparse(normalizedURL).netloc in optout:
                    continue
                if normalizedURL not in Visited and \
                   normalizedURL not in URLs and \
                   normalizedURL not in Skipped :
                    URLs.append({'link':normalizedURL, 'depth':url['depth']+1})

    print(len(URLs), len(Visited))

from urllib.parse import urlparse

URLs = [ ]
Visited = []
Skipped = []
depth = 3
optin = ['blog.naver.com']
optout = []



# Forcused Crawling
# Depth 제한
# Domain 제한
# HTML Tags 제한



URLs.append({'link':'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=수지', 'depth':0})

while URLs:
    url = URLs.pop(-1) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    if url['depth'] > depth:
        Skipped.append(url['link'])
        continue

    resp = download(url['link'], headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    Visited.append(url['link'])

    if resp is None:
        continue

    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        for link in dom.select('''a[href], frame[src], iframe[src], img[src],
        audio[src], video[src], style[src], link[src]'''):
            newURL = link.attrs['href'] if link.has_attr('href') else link.attrs['src']

            if not re.match(r'#|javascript|mailto', newURL):
                normalizedURL = urljoin(url['link'], newURL)
                if urlparse(normalizedURL).netloc not in optin:
                    continue
                if normalizedURL not in Visited and \
                   normalizedURL not in URLs and \
                   normalizedURL not in Skipped :
                    URLs.append({'link':normalizedURL, 'depth':url['depth']+1})

    print(len(URLs), len(Visited))

from urllib.parse import urlparse

URLs = [ ]
Visited = []
Skipped = []
depth = 5
optin = ['news.naver.com','n.news.naver.com']
optout = ['v.daum.net','']



# Forcused Crawling
# Depth 제한
# Domain 제한
# HTML Tags 제한



URLs.append({'link':'https://news.naver.com/', 'depth':0})

while URLs:
    url = URLs.pop(0) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    if url['depth'] > depth:
        Skipped.append(url['link'])
        continue

    resp = download(url['link'], headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    Visited.append(url['link'])

    if resp is None:
        continue

    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        linkA = dom.select('ul.Nlnb_menu_list li > a')

        linkB = dom.select('div[class$="_text"] > a[href]:has(> strong)')

        for link in linkA + linkB:
            newURL = link.attrs['href'] if link.has_attr('href') else link.attrs['src']

            if not re.match(r'#|javascript|mailto|data', newURL):
                normalizedURL = urljoin(url['link'], newURL)
                if urlparse(normalizedURL).netloc not in optin:
                    continue
                if normalizedURL not in Visited and \
                   normalizedURL not in URLs and \
                   normalizedURL not in Skipped :
                    URLs.append({'link':normalizedURL, 'depth':url['depth']+1})

    print(len(URLs), len(Visited))

from os import mkdir, listdir

listdir('.')

mkdir('./naver_news')

listdir('.')

mkdir('naver_img')

len('0005392171')

resp.content.decode('utf8', errors='ignore')

resp.encoding

from requests.compat import urljoin, urlparse

# Focused Crawling
# 1. Depth 제한
# 2. Domain 제한
# 3. HTML Tags 제한
# ....

URLs = []
Visited = []
Skipped = []

# 1. 깊이로 제한
depth = 5
# 2. 도메인 제한
optin = ['news.naver.com', 'n.news.naver.com', 'imgnews.pstatic.net'] # 여기 있는 것들만
optout = ['v.daum.net', ''] # 얘네 빼고

URLs.append({'link':'https://news.naver.com', 'depth':0})
# URLs.append({'link':'https://search.daum.net/search?w=tot&q=수지', 'depth':0})
# URLs.append({'link':'https://search.naver.com/search.naver?where=nexearch&query=수지', 'depth':0})
# URLs.append('https://www.google.com/search?q=수지')

NEWS_TEXT = './naver_news'
NEWS_IMG = './naver_img'

while URLs:
    url = URLs.pop(-1)

    # 1. 깊이로 제한
    if url['depth'] > depth:
        Skipped.append(url['link'])
        continue

    resp = download(url['link'], # 수정
                    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.24 Safari/537.36'})

    Visited.append(url['link']) # 수정

    if resp is None:
        continue

    # Scraping
    if re.search(r'image\/(\w+);?', resp.headers['content-type']):
        ext = re.search(r'image\/(\w+);?', resp.headers['content-type']).group(1)
        # 파일이름 고치세요
        fname = re.search(r'/(\w+\.jpg|jpeg|png|bmp|gif)', url['link']).group(1)
        with open(NEWS_IMG+'/'+fname+'.'+ext, 'wb') as fp:
            fp.write(resp.content)

    # Crawling
    if re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')

        # 3. 영역제한 - 뉴스인 경우
        # 3-1. 메뉴
        linksA = dom.select('ul.Nlnb_menu_list li > a')
        # 3-2. 뉴스
        linksB = dom.select('div[class$="_text"] > a[href]:has(> strong)')
        # 3-3. 뉴스 본문
        linksC = dom.select('#dic_area a[href], #dic_area img[data-src]')
        article = dom.select_one('#dic_area')
        # Scraping for Indexing
        if article:
            with open(NEWS_TEXT+'/'+re.search(r'(\d{10})$', url['link']).group(1)+'.txt',
                      'w', encoding='utf8') as fp:
                fp.write(article.get_text())

        for link in linksA+linksB+linksC:
            if link.has_attr('href'):
                newURL = link.attrs['href']
            if link.has_attr('src'):
                newURL = link.attrs['src']
            if link.has_attr('data-src'):
                newURL = link.attrs['data-src']

            if not re.match(r'#|javascript|mailto|data', newURL):
                normalizedURL = urljoin(url['link'], newURL) # 수정
                # 2. 도메인 제한
                if urlparse(normalizedURL).netloc not in optin:
                    continue
#                 if urlparse(normalizedURL).netloc in optout:
#                     continue

                if normalizedURL not in Visited and \
                   normalizedURL not in [url['link'] for url in URLs] and \
                   normalizedURL not in Skipped:
                    URLs.append({'link':normalizedURL, 'depth':url['depth']+1}) # 수정

#     print(len(URLs), len(Visited))

resp = download('https://imgnews.pstatic.net/image/308/2024/03/15/0000034493_001_20240315064801301.jpg?type=w647')

re.search(r'image\/(\w+);?', resp.headers['content-type']).group(1)

re.search(r'/(\w+\.jpg|jpeg|png|bmp|gif)',
          'https://imgnews.pstatic.net/image/277/2024/03/14/0005392171_001_20240314142305641.jpg?type=w647'
         ).groups(1)



