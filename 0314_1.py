# HTTP, response.body 해석?
# (Bytes) -> Content-type (MIME) __/__; text/html, application/json
# Bytes -> decode -. Str ; 이때부터 문자열 처리 가능 -> RE (불편)
# Bytes -> decode -. Str -> json.loads -> python obj(Dict)
# HTML (Markup;Document;Semi-structuted) -> HTML Parser -> DOM(Tree) <- BS4
# elemet.Tag -> find, find_all(자식, 자손, 밑에 방향)
#            -> find_parent, find_parents (부모, 조상, 위에 방향)
#            -> find_prev_siblong(s), find_next_sibling(s) (부모를 공유하는 형제 노트, 이전, 이후)

from requests import get

url = 'https://pythonscraping.com/pages/page3.html'
resp = get(url)

resp.status_code, resp.reason, resp.request.headers, resp.headers

import re

re.search(r'text', resp.headers['content-type'])

from bs4 import BeautifulSoup

dom = BeautifulSoup(resp.text, 'html.parser')
dom

[tag.name for tag in dom.html.find_all(resursive=False)]

# dom = BeautifulSoup(resp.text, 'html5lib')
# [tag.name for tag in dom.div.find_all(resursive=False)]

# dom = BeautifulSoup(resp.text, 'html5lib')
# [tag.name for tag in dom.div.find_all(resursive=False)]

dom.body.div

dom.body.a

type(dom.body.a)

dom.body.div.attrs

dom.find(string=re.compile(r'\$0\.50'))

dom.find(string=re.compile(r'\$0\.50')).find_parent()

# <table> 뭐시기 있는거 복붙하기 - html의 구조 대략적으로 알려준것임

node = dom.find(string=re.compile(r'\$0\.50')).find_parent()

node.find_next_sibling()

node.find_next_sibling().find('img')

node.find_next_sibling().find('img') is not None

node.find_next_sibling().find('img').attrs['src']

# / : 루트
# . : 현재 위치
# .. : 부모위치

resp.request.url

from requests.compat import urljoin

urljoin(resp.request.url, node.find_next_sibling().find('img').attrs['src'])

url = urljoin(resp.request.url, node.find_next_sibling().find('img').attrs['src'])

get(url)

resp = get(url)
resp.status_code, resp.reason, resp.request.headers, resp.headers

resp.headers['content-type']

resp.content # 가 이미지라는 의미

fname = re.search(r'.+/(.+\.jpg)$', resp.url).group(1)

fp = open(fname, 'bw')

fp.write(resp.content)
fp.close()

[tag.name for tag in node.find_parents()]

node.find_parents(limit=2)[-1].name

node.find_parents(limit=2)[-1].find_next_siblings()

dom.find(attrs={'id':'footer'})

node.find_parents(limit=2)[-1].find_next_sibling() is dom.find(attrs={'id':'footer'})

dom.div.find_all(recursive=False)[-1] is dom.find(attrs={'id':'footer'})

# < tag attributes = id, class> id -> 고유한 값 class -> 다중 상속

node.find_parents(limit=2)[-1].find_all(recurcise=False)[0]
node.find_parents(limit=2)[-1].find().find_all(recurcise=False)[1].get_text()

# table 에 있는 이미지 전부 찾는 법

dom.table.find_all('img')

dom.table.find_all(attrs={'src':re.compile(r'jpg$')})

for tag in dom.table.find_all(recursive=False)[1:]:
    print(tag.find_all(recursive=False)[-1].find())

for tag in node.find_parent().find_previous_siblings()[:-1]:
    print(tag.find_all()[-1])

for tag in node.find_parent().find_next_siblings():
    print(tag.find_all()[-1])



# CSS Selectoy
# 태그 이름 {스타일}
# -------------------관심 x
# 아이디
# .클래스
# .클래스A.클래스B
# .클래스A .클래스B - 자손
# .클래스A>.클래스B - 자식
# [속성=값]
# 태그 이름, .클래스
# 가상선택자 : first-child, last-child, nth-if-type, nth-child

dom.select('table img')

dom.select('table img[src$="jpg"]')

dom.select('table>tr:nth-child(n)') # tr = *

dom.select('table>tr:first-child ~ *') # tr = *

dom.select('table>tr:first-child ~ tr > *:nth-child(4) > :first-child') # tr = *

dom.select('td:has(img)>*')

# 유일하게 못하는 것 부모 노트 찾기

dom.select('tr > td:nth-of-type(4) > img')

dom.select('tr > td:nth-of-type(4) > img')[0]



url = 'https://www.google.com/search?q=수지'
resp = get(url)

dom = BeautifulSoup(resp.content, 'html.parser')

dom.select('h3')

dom.select('a:has(>h3)')

url = 'https://www.google.com/search?q=수지'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
resp = get(url, headers={'user-agent':ua})

dom = BeautifulSoup(resp.content, 'html.parser')

for tag in dom.select('a:has(>h3)'):
    print(tag.attrs['href'] if tag.has_attr('href') else None)
    print(tag.select_one('h3').get_text())

for tag in dom.select('a:has(.LC20lb)'):
    print(tag.attrs['href'] if tag.has_attr('href') else None)
    print(tag.select_one('h3').get_text())

for tag in dom.find_all(attrs={'class':re.compile(r'^LC20lb')}):
    print(tag.attrs['href'] if tag.has_attr('href') else None)
    print(tag.get_text())

dom.select('div > div > span > a > h3 ')

# ctr + f

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
resp = get(url, headers={'user-agent':ua})

url = 'https://search.naver.com/search.naver?where=nexearch&query=수지'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
resp = get(url, headers={'user-agent':ua})

dom = BeautifulSoup(resp.text, 'html.parser')

for link in dom.select('.news_tit, .link_tit, .title_link'):
    print(link.attrs['href'])
    print(link.get_text())

len(dom.select('.news_tit, .link_tit, .title_link'))



url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=수지'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
resp = get(url, headers={'user-agent':ua})

dom = BeautifulSoup(resp.text, 'html.parser')

dom.find_all(string='수지')

for link in dom.select('c-doc-web > c-title'):
    print(link.attrs['data-href'])
    print(link.contents)



# robots.txt
# 400, 500번대 분기

from requests.compat import urlparse

def canFetch(url, path):
    resp = get(urljoin(url, '/robots.txt'))

    if resp.status_code != 200:
        return True

    disallowList = [link for link in re.findall(r'Disallow\s*:\s*(.+)', resp.text, re.IGNORECASE)]

    if urlparse(path).path in disallowList:
        return False

    return True

canFetch('https://www.google.com', '/search?q=수지')

import requests
from requests.exceptions import HTTPError
from time import sleep

def download(url, params={}, data={}, headers={}, method='GET', retries=3):

    if not canFetch(url, url):
        print('수집하면 안됨.')

    resp = requests.request(method, url, params=params, data=data, headers=headers)

    try:
        resp.raise_for_status()
        return resp
    except HTTPError as e:
        if retries > 0 and 499 < e.response.status_code < 600:
            print('Retrying...')
            sleep(5)
            return download(url, params, data, headers, method, retries - 1)
        else:
            print(e.response.status_code)
            print(e.request.headers)
            print(e.response.headers)
            return None


response = download('https://httpbin.org/status/500')
print(response)

download('https://www.google.com//search?q=수지')



# XPath

# /html/body
# /html//a



#Crawler : link를 따라다니는 애
# link 찾기 ~ a[href], from[action], iframe[src] //// video/audio[src], css/js[src]
# 따라다니게 만들기 ~ 웹은 범위 제한 불가, unknown search space ~ tree 탐색 DFS-stack구조, BFS-queue구
# 그전에 새롭게 찾은 link 검사 - absolute path 정규
# 그전에 새롭게 찾은 link 방문 여부 확인



URLs = ['http://inisw.kr']
Visited = []

while URLs:
    url = URLs.pop(-1) # 0:FIFO;Queue, -1:LIFO:FILO;Stack

    Visited.append(url)

    resp = download(url)

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



