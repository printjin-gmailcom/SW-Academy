# https://domain.whois.co.kr/

# domain/robots.txt

# elements ~ doom. html로 표현되어있는, 랜더링이 다 끝난 상태가 보여지는 것 뿐

# network -- preserve log 키는거 추



from urllib import robotparser

url = 'https://www.google.com/robots.txt'
rp = robotparser.RobotFileParser(url)
rp.read()

rp.can_fetch('Bot', '/')

url = 'https://www.naver.com/robots.txt'
rp = robotparser.RobotFileParser(url)
rp.read()

rp.can_fetch('Bot', '/')

url = 'https://news.naver.com/robots.txt'
rp = robotparser.RobotFileParser(url)
rp.read()

rp.can_fetch('Bot', '/')

rp.can_fetch('Yeti', '/')

rp.can_fetch('Bot', '.main/imageontage/')

rp.can_fetch('Yeti', '.main/imageontage/')

url = 'https://lms.sunde41.net/robots.txt'
rp = robotparser.RobotFileParser(url)
rp.read()

rp.can_fetch('Bot', '/')

rp.can_fetch('Yeti', '.main/imageontage/')

rp.url

rp.host

rp.path

rp.set_url('https://www.google.com/robots.txt')
rp.read



from urllib import request

url = 'https://www.google.com'
resp = request.urlopen(url)

type(resp)

# TCP/IP -> Bytes(00101010101010101)
# HTTP -> text/html
#         text -> Bytes (요청)
#                 Bytes -> text(응답)

resp.read()

rst = resp.read()

type(rst)

# rst.decode() # &#+ctrl+f 하면 검색됨 -> 이떄, '&#47196;&#44536;&#51064;' 나옴

from html import escape, unescape

unescape( '&#47196;&#44536;&#51064;')

hex(47196), ord('로')

resp.getheaders()

resp.status, resp.reason

# 보기
# 1, 어쩌고

# escape('<') -> HTML Entities ( html 에서 특수기호 표현하는 방법, &#______;)

unescape('&gt;'), unescape('&nbsp;') # 띄어쓰기

chr = ord('고')
unescape(f'&#{chr};')



# https://lms.sunde41.net/auth/login
#   ?
#   next=/course/6
#   key=value &

# GET
# SCHEME : https
#     ://
# HOST    nid.naver.com
# PATH    /nidlogin.login
# PARAMS    ?
# QUERYSTRING
#    mode = form
#    &
#    url = httpsL//mail.naver.com

# POST
# requst.body = mode = form&url = httpl://mail.naver.com/

# https://www.google.com/search?q=
#     %EC%88%98%EC%A7%80
#     -> PERCENT ENCODING + HEXADECIMAL
#            %F             0-F(0-15)

# 0000 - 1111 -> 0-15
# 0000 0000 -> 8ㅠㅑㅅㄴ = 1BYTE
# 0~F 0~F -> %00, %FF

#       Non-ASCII
# HTML -> HTML Entities (&#_10진수_;)
# HTTP -> PERCENT ENCODING (%_16진수 바이트_)



from urllib.parse import quote, quote_plus, unquote, unquote_plus
from urllib.parse import parse_qs, urljoin, urlparse, urlunparse

quote('수지')

quote('수 지'), quote_plus('수 지')

quote('수 지'), quote_plus('수 지 +')

# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%88%98%EC%A7%80
# https://www.google.com/search?q=%EC%88%98%EC%A7%80&oq=%EC%88%98%EC%A7%80&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQLhixAxiABDIHCAIQABiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDINCAUQABiDARixAxiABDITCAYQLhiDARjHARixAxjRAxiABDIGCAcQRRg80gEIMjU1NmowajSoAgCwAgA&sourceid=chrome&ie=UTF-8

unquote(quote('수 지')), unquote_plus(quote_plus('수 지'))

url = 'https://www.google.com/search?q=%EC%88%98%20%EC%A7%80&sourceid=chrome&ie=UTF-8'
rst = urlparse(url)

rst.scheme

rst.netloc

rst.path

rst.params

rst.query

rst.fragment

urlunparse(('https','www.google.com','/search','','q=수지',''))

# <a href = '#어쩌고'>클릭</a?> -> 페이지 전환 없음, 새로운 내용 없음, 같은 페이지

from urllib.parse import parse_qsl
parse_qs(rst.query), parse_qsl(rst.query)

params = parse_qs(rst.query)

params['q'] = '황정민'

params

from urllib.parse import urlencode, urlunparse

urlencode(params)

urlunparse(('https','www.google.com','/search','',urlencode(params),''))

urljoin(url, '/search/about')
urljoin(url, 'https://www.naver.com')
urljoin(url, '/path/path2/path3?q=asdfasdfa')

'https://www.google.com/search?q='+quote('수지')

# UR(QS), QUOTE, URLENCODE등 활용 가능

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

req = request.Request(
    url='https://www.google.com/search?q='+quote('수지'),
    headers = {'user-agent':ua}, method='GET')

req.headers

req.method

req.full_url

resp = request.urlopen(req)

resp.status, resp.reason, resp.getheaders()

raw = resp.read()
raw.decode('utf8')

resp.getheader('content-type')

# Google, Daum
# Robots.txt 0, service 적용

# Naver,
# Robots.txt 0, service 미적용

url = 'https://search.naver.com/search.naver'
qs = parse_qs('where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%88%98%EC%A7%80')

urljoin(url, '?'+urlencode(qs))

request.urlopen(urljoin(url, '?'+urlencode(qs)))
resp.status, resp.reason, resp.getheaders()

resp.read().decode('utf8')

url = 'https://search.daum.net/search'
req = request.Request(url=url, headers={'user-dgnet':ua}, method='GET')
resp = request.urlopen(req)

resp.status, resp.reason, resp.getheaders()



# 네이트는 검색엔진 기능없고 다음거를 활용함

url = 'https://search.daum.net/search'
req = request.Request(url=url, headers={'user-dgnet':ua}, method='GET')
resp = request.urlopen(req)
resp.status, resp.reason, resp.getheaders()



from urllib.error import HTTPError
from time import sleep

def retry(url, maxetrires=5):
    try:
        resp = request.urlopen(url)
    except HTTPError as e:
        print(e.status)
        print(e.reason)

        if 400 <= e. status < 500:
            return None
            if 500 <= e. status < 600:
                sleep(5)
                retry(url)
            else:
                return None

retry('https://www.google.com/search?q=%EC88%98%EC%A7%80')



from requests import request, get
from requests.compat import urljoin, urlencode, quote, unquote
from requests.exceptions import HTTPError

request()

url = 'https://www.google.com/search?q=%EC%88%98%EC%A7%80'

resp = request('GET', url)

resp.status_code, resp.reason, resp.headers

type(resp.content), type(resp.text), resp.encoding

resp.text

resp.request.url, resp.request.headers

resp.status_code, resp.headers



resp = request('GET', url='https://www.google.com/search?q=수지')
resp.request.url



# https://httpbin.org/

from requests import request
url = 'https://httpbin.org/status/'
resp = request('GET', url+'403')

from urllib import request
resp = request.urlopen(url+'404')

resp.status_code, resp.reason

from requests.exceptions import HTTPError

try:
    resp.raise_for_status()
except HTTPError as e:
    print(e.response.status_code)
    print(e.response.reason)
    print(e.response.headers)
    print(e.request.headers)

''''''''''''''144

pip install requests

import requests

url = 'https://httpbin.org/status/'
resp = requests.get(url + '500')

if 500 <= resp.status_code < 600:
    print('에러')



import requests

url = 'https://httpbin.org/post/'
resp = requests.get(url)
print(resp.status_code, resp.request.url)

resp.request.url, resp.request.body

print(resp.text)

url = 'https://httpbin.org/post/
resp = request('GET', url, data={'키':'밸류', 'key':'value'})
resp.status_code, resp.request.url

resp.request.url, resp.request.body

print(resp.txt)

import requests

url = 'https://httpbin.org/post'
resp = requests.post(url, params={'key2':'value2'}, data={'키':'밸류', 'key':'value'})
print(resp.status_code, resp.request.url)

resp.request.url, resp.request.body

print(resp.text)

