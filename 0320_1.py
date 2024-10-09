# Client    HTTP     Server
# 1    ------------->
# DOM1 <------------ HTML(text/html) => Browser를 대신(bs4)

# 2    ------------->
# DOM2 <------------ HTML(text/html) => Browser를 대신(bs4)

#     ///////// => JS engine => selenium(추천X)

# 3    -------------> XmlHttpRequest JS
#      DHTML / AJAX => 찾는거 핵심(network탭)
# DOM2 <------------ Data(application/json, javascript, ...) => Browser를 대신(bs4 X)

# Client              Server
#       -------------> (id,pw) => DB => 사용자정보
#       <------------ http.response.header[set-cookie]

#       -------------> 이메일 클릭
# 내 이메일 <------------

# Cookie(O)            Session(X)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile lms.json
# {
#     "id":"printjin@gmail.com",
#     "pw":"@01045063891"
# }

from json import load

with open('./lms.json', 'r') as fp:
    lms = load(fp)

from requests import request

url = 'https://lms.sunde41.net'
resp = request('GET', url)

resp.text

from bs4 import BeautifulSoup

dom = BeautifulSoup(resp.text, 'html.parser')

len(dom.select_one('form'))

for node in dom.select('form imput[name]'):
    print(node.attrs['name'], node.attrs['value'] if node.has_attr('value') else '')

# https://lms.sunde41.net
# => https://lms.sunde41.net/auth/login?next=%2F

dom.select_one('form').attrs

from requests.compat import urljoin

params = {
    'next':'/',
    'email':'printjin@gmail.com',
    'password':'@01045063891',
    'remember':'3'
}

request('POST', urljoin(url, dom.select_one('form').attrs['action']), data=params)

resp.status_code, resp.request.body, resp.headers

request('GET', url).text

resp.headers.get('cookie') #None

# resp.headers['set-cookie'].split('\n')[0].split(';')[0].split('=')



cookie = {
    'session':'Ix-xQaoe6Yd40Q5xycP0X0Ya5lwQ4D_JWdTNOvw4GaE'
}
request('GET', url, cookies=cookie).text

from requests.cookies import cookiejar_from_dict, create_cookie

c = cookiejar_from_dict(cookie)

request('GET', url, cookies=c).text

c

url

c.set('k', 'v')

from requests.sessions import Session

sess = Session()

# request() => set-cookie => 내가 관리
# sess.request() => set-cookie => session이 관리

sess.cookies

sess.cookies.set('session', 'Ix-xQaoe6Yd40Q5xycP0X0Ya5lwQ4D_JWdTNOvw4GaE')

sess.request('GET', url).text

sess.cookies

# name='session', value='Ix-xQaoe6Yd40Q5xycP0X0Ya5lwQ4D_JWdTNOvw4GaE', domain_initial_dot=False, path='/'

sess.request('GET', url).headers

sess.request('GET', url)

sess.request('GET', url).text

sess.cookies.clear()



sess.request('GET', url).text

sess.cookies.set('session', 'Ix-xQaoe6Yd40Q5xycP0X0Ya5lwQ4D_JWdTNOvw4GaE', domain='lms.sunde41.net')

sess.request('GET', url).text

sess.cookies

request('GET', url, cookies = sess.cookies).text



sess.cookies.clear()

url = 'https://lms.sunde41.net/course/6'
request('GET', url).text

request('GET', url).status_code

request('GET', url).headers

sess.request('GET', url).text

sess.cookies

url = 'https://lms.sunde41.net/auth/login'
params = {
    'next':'/',
    'email':lms['id'],
    'password':lms['pw'],
    'remember':'on'
}
resp = sess.request('POST', url, data=params)
resp.headers

sess.cookies

url = 'https://lms.sunde41.net/course/6'

resp = sess.request('GET', url)
resp.headers

resp.text

dom = BeautifulSoup(resp.text, 'html.parser')
dom.title



dom.select('#lesson tbody > tr')

len(dom.select('#lesson tbody > tr'))

dom.select('#lesson tbody > tr > td:last-child')

len(dom.select('#lesson tbody > tr > td:last-child'))

for node in dom.select('#lesson tbody > tr > td:last-child'):
    print(node.text)

for node in dom.select('#lesson tbody > tr > td:last-child')[:2]:
    print(node)

for node in dom.select('#lesson tbody > tr > td:last-child a.dropdown-item[href]')[:2]:
    print(node)

for node in dom.select('#lesson a.dropdown-item[href]'):
    print(node.attrs['href'])

resp = sess.request('GET', urljoin(url, '/static/uploads/lectures/6/Database.pdf'))
resp.headers

with open('db.pdf', 'wb') as fp:
    fp.write(resp.content)

!dir

sess.cookies

request('GET', urljoin(url, '/static/uploads/lectures/6/Database.pdf')).headers

# www-data:www-data => 권한 x
# /static/uploads/.... => www-data

urljoin(url, '/static/uploads/lectures/6/Database.pdf')

# urljoin(url, '/static/uploads/lectures/6/Database.pdf') => public, uploads, ..., static douwnload

# REST API

# GET => Read   https://lms.sunde41.net/qna/detail/77
# POST=> Create https://lms.sunde41.net/qna/detail/77

url = 'https://lms.sunde41.net/qna/detail/77'
resp = sess.request('POST', url, data={'description':'REST 테스트'})

resp = sess.request('GET', url)
dom = BeautifulSoup(resp.text, 'html.parser')

for a in dom.select('.page-body .row > .col-auto:has(> a) > a:last-child'):
    sess.request('GET', urljoin(url, a.attrs['href']))

sess.request('GET', 'https://lms.sunde41.net/qna/delete/77')



sess.cookies.clear()

url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'

resp = sess.request('GET', url)
dom = BeautifulSoup(resp.text, 'html.parser')

dom.title

dom.select('form[action]')

len(dom.select('form[action]'))

for node in dom.select('form[action] input[name]'):
    print(node.attrs['name'], node.attrs['value'] if node.has_attr('value') else '')

# id, pw -> JS(RSA)

import re

re.split

dir(str)

# str.split()
# str.splitlines()

# c = '''
# ONID	710C1965A8271C8563AAA53A723454B4	www.naver.com	/	Session	42	✓				Medium
# NID_AUT	AuEhaOvqGImKpFl0kLsdqFIdluZalVo4if074PfVfJFGV0DGWeDnoBkwlm91fuJZ	.naver.com	/	Session	71	✓	✓	Lax		Medium
# NID_JKL	HLwiuJdVA958zWyDH3SaK67mcUj7knNdMSaZ06PB+dU=	.naver.com	/	Session	51		✓			Medium
# NID_SES	AAABs3hWYHimoWXLskilSd12vI6+D71zGmwGePaMpl8xKBw4GEmhihw3sybyXmz43NxaCkZE8XjzvmGeRhjz6DDPUKMV6OGRB5D8xwophxJk3QqwK7GhB3H7YvQs8gAMpUaRJuPWB2wqTrx13+FQr9u+35ETHJyz9TkCPLrr7tk7M74Kd3DHp7tuZ08XLBpG5x7RJbsaGDbH//pup3gtGyTOzHWfzppy6dfp8oK9CSI0jivNeS0Y2BPhgznilzs+GpZPndDVAROi6AkHxNMNCtXB5aJnUFLydYjfZ2pO+6Ofb2wafmiGqqw006LSdesnVzc5MVkAjb3LopnWo010kELSDlrWrTLpbhqFXvip75gfAlflRnoRefTjXmHCW/CC11KpOpZP6iLyMHcZF2ztRvlLnQxYBwHS0xLRO7fxvPRLnzns5m0MP9Uxo32trXUVBCHlmUcT47+m+iRakgqd9IDNorJ0dg3vsi8S+BZ3+P638d85dpGHoFTu6UwNqspwTfVr4v3i1/+gHbGm7lbOZjqpan+XpUqQrFdcoRFtgra4RF9FxrwNcfL4DxVr55avmJuUi9pZ2mKpIapSZ7pewG9jKy4=	.naver.com	/	Session	611		✓	Lax		Medium
# NM_srt_chzzk	1	www.naver.com	/	2024-03-24T08:08:14.000Z	13					Medium
# NNB	63DRE2UT6DXWK	.naver.com	/	2025-04-27T08:08:24.608Z	16		✓	None		Medium
# _ga	GA1.1.1302965497.1710648609	.naver.com	/	2025-04-26T05:43:01.944Z	30					Medium
# _ga_3X9JZ731KT	GS1.1.1711086181.8.0.1711086187.0.0.0	.naver.com	/	2025-04-26T05:43:07.980Z	51					Medium
# _gcl_au	1.1.697653695.1710648609	.naver.com	/	2024-06-15T04:10:09.000Z	31					Medium
# nid_inf	573067207	.naver.com	/	Session	16					Medium
# tooltip_paging_close	1	www.naver.com	/	2025-04-21T04:59:09.426Z	21					Medium
# tooltip_shoppingbox_close	1	www.naver.com	/	2025-04-17T08:33:41.879Z	26					Medium
# '''

# AuEhaOvqGImKpFl0kLsdqFIdluZalVo4if074PfVfJFGV0DGWeDnoBkwlm91fuJZ

c = '''
ONID	710C1965A8271C8563AAA53A723454B4	www.naver.com	/	Session	42	✓				Medium
NID_AUT	AuEhaOvqGImKpFl0kLsdqFIdluZalVo4if074PfVfJFGV0DGWeDnoBkwlm91fuJZ	.naver.com	/	Session	71	✓	✓	Lax		Medium
NID_JKL	HLwiuJdVA958zWyDH3SaK67mcUj7knNdMSaZ06PB+dU=	.naver.com	/	Session	51		✓			Medium
NID_SES	AAABs3hWYHimoWXLskilSd12vI6+D71zGmwGePaMpl8xKBw4GEmhihw3sybyXmz43NxaCkZE8XjzvmGeRhjz6DDPUKMV6OGRB5D8xwophxJk3QqwK7GhB3H7YvQs8gAMpUaRJuPWB2wqTrx13+FQr9u+35ETHJyz9TkCPLrr7tk7M74Kd3DHp7tuZ08XLBpG5x7RJbsaGDbH//pup3gtGyTOzHWfzppy6dfp8oK9CSI0jivNeS0Y2BPhgznilzs+GpZPndDVAROi6AkHxNMNCtXB5aJnUFLydYjfZ2pO+6Ofb2wafmiGqqw006LSdesnVzc5MVkAjb3LopnWo010kELSDlrWrTLpbhqFXvip75gfAlflRnoRefTjXmHCW/CC11KpOpZP6iLyMHcZF2ztRvlLnQxYBwHS0xLRO7fxvPRLnzns5m0MP9Uxo32trXUVBCHlmUcT47+m+iRakgqd9IDNorJ0dg3vsi8S+BZ3+P638d85dpGHoFTu6UwNqspwTfVr4v3i1/+gHbGm7lbOZjqpan+XpUqQrFdcoRFtgra4RF9FxrwNcfL4DxVr55avmJuUi9pZ2mKpIapSZ7pewG9jKy4=	.naver.com	/	Session	611		✓	Lax		Medium
NM_srt_chzzk	1	www.naver.com	/	2024-03-24T08:08:14.000Z	13					Medium
NNB	63DRE2UT6DXWK	.naver.com	/	2025-04-27T08:08:24.608Z	16		✓	None		Medium
_ga	GA1.1.1302965497.1710648609	.naver.com	/	2025-04-26T05:43:01.944Z	30					Medium
_ga_3X9JZ731KT	GS1.1.1711086181.8.0.1711086187.0.0.0	.naver.com	/	2025-04-26T05:43:07.980Z	51					Medium
_gcl_au	1.1.697653695.1710648609	.naver.com	/	2024-06-15T04:10:09.000Z	31					Medium
nid_inf	573067207	.naver.com	/	Session	16					Medium
tooltip_paging_close	1	www.naver.com	/	2025-04-21T04:59:09.426Z	21					Medium
tooltip_shoppingbox_close	1	www.naver.com	/	2025-04-17T08:33:41.879Z	26					Medium
'''

c.splitlines()

c = '''
ONID	710C1965A8271C8563AAA53A723454B4	www.naver.com	/	Session	42	✓				Medium
NID_AUT	AuEhaOvqGImKpFl0kLsdqFIdluZalVo4if074PfVfJFGV0DGWeDnoBkwlm91fuJZ	.naver.com	/	Session	71	✓	✓	Lax		Medium
NID_JKL	HLwiuJdVA958zWyDH3SaK67mcUj7knNdMSaZ06PB+dU=	.naver.com	/	Session	51		✓			Medium
NID_SES	AAABs3hWYHimoWXLskilSd12vI6+D71zGmwGePaMpl8xKBw4GEmhihw3sybyXmz43NxaCkZE8XjzvmGeRhjz6DDPUKMV6OGRB5D8xwophxJk3QqwK7GhB3H7YvQs8gAMpUaRJuPWB2wqTrx13+FQr9u+35ETHJyz9TkCPLrr7tk7M74Kd3DHp7tuZ08XLBpG5x7RJbsaGDbH//pup3gtGyTOzHWfzppy6dfp8oK9CSI0jivNeS0Y2BPhgznilzs+GpZPndDVAROi6AkHxNMNCtXB5aJnUFLydYjfZ2pO+6Ofb2wafmiGqqw006LSdesnVzc5MVkAjb3LopnWo010kELSDlrWrTLpbhqFXvip75gfAlflRnoRefTjXmHCW/CC11KpOpZP6iLyMHcZF2ztRvlLnQxYBwHS0xLRO7fxvPRLnzns5m0MP9Uxo32trXUVBCHlmUcT47+m+iRakgqd9IDNorJ0dg3vsi8S+BZ3+P638d85dpGHoFTu6UwNqspwTfVr4v3i1/+gHbGm7lbOZjqpan+XpUqQrFdcoRFtgra4RF9FxrwNcfL4DxVr55avmJuUi9pZ2mKpIapSZ7pewG9jKy4=	.naver.com	/	Session	611		✓	Lax		Medium
NM_srt_chzzk	1	www.naver.com	/	2024-03-24T08:08:14.000Z	13					Medium
NNB	63DRE2UT6DXWK	.naver.com	/	2025-04-27T08:08:24.608Z	16		✓	None		Medium
_ga	GA1.1.1302965497.1710648609	.naver.com	/	2025-04-26T05:43:01.944Z	30					Medium
_ga_3X9JZ731KT	GS1.1.1711086181.8.0.1711086187.0.0.0	.naver.com	/	2025-04-26T05:43:07.980Z	51					Medium
_gcl_au	1.1.697653695.1710648609	.naver.com	/	2024-06-15T04:10:09.000Z	31					Medium
nid_inf	573067207	.naver.com	/	Session	16					Medium
tooltip_paging_close	1	www.naver.com	/	2025-04-21T04:59:09.426Z	21					Medium
tooltip_shoppingbox_close	1	www.naver.com	/	2025-04-17T08:33:41.879Z	26					Medium
'''

c.splitlines()[1:]

c = '''
ONID	710C1965A8271C8563AAA53A723454B4	www.naver.com	/	Session	42	✓				Medium
NID_AUT	AuEhaOvqGImKpFl0kLsdqFIdluZalVo4if074PfVfJFGV0DGWeDnoBkwlm91fuJZ	.naver.com	/	Session	71	✓	✓	Lax		Medium
NID_JKL	HLwiuJdVA958zWyDH3SaK67mcUj7knNdMSaZ06PB+dU=	.naver.com	/	Session	51		✓			Medium
NID_SES	AAABs3hWYHimoWXLskilSd12vI6+D71zGmwGePaMpl8xKBw4GEmhihw3sybyXmz43NxaCkZE8XjzvmGeRhjz6DDPUKMV6OGRB5D8xwophxJk3QqwK7GhB3H7YvQs8gAMpUaRJuPWB2wqTrx13+FQr9u+35ETHJyz9TkCPLrr7tk7M74Kd3DHp7tuZ08XLBpG5x7RJbsaGDbH//pup3gtGyTOzHWfzppy6dfp8oK9CSI0jivNeS0Y2BPhgznilzs+GpZPndDVAROi6AkHxNMNCtXB5aJnUFLydYjfZ2pO+6Ofb2wafmiGqqw006LSdesnVzc5MVkAjb3LopnWo010kELSDlrWrTLpbhqFXvip75gfAlflRnoRefTjXmHCW/CC11KpOpZP6iLyMHcZF2ztRvlLnQxYBwHS0xLRO7fxvPRLnzns5m0MP9Uxo32trXUVBCHlmUcT47+m+iRakgqd9IDNorJ0dg3vsi8S+BZ3+P638d85dpGHoFTu6UwNqspwTfVr4v3i1/+gHbGm7lbOZjqpan+XpUqQrFdcoRFtgra4RF9FxrwNcfL4DxVr55avmJuUi9pZ2mKpIapSZ7pewG9jKy4=	.naver.com	/	Session	611		✓	Lax		Medium
NM_srt_chzzk	1	www.naver.com	/	2024-03-24T08:08:14.000Z	13					Medium
NNB	63DRE2UT6DXWK	.naver.com	/	2025-04-27T08:08:24.608Z	16		✓	None		Medium
_ga	GA1.1.1302965497.1710648609	.naver.com	/	2025-04-26T05:43:01.944Z	30					Medium
_ga_3X9JZ731KT	GS1.1.1711086181.8.0.1711086187.0.0.0	.naver.com	/	2025-04-26T05:43:07.980Z	51					Medium
_gcl_au	1.1.697653695.1710648609	.naver.com	/	2024-06-15T04:10:09.000Z	31					Medium
nid_inf	573067207	.naver.com	/	Session	16					Medium
tooltip_paging_close	1	www.naver.com	/	2025-04-21T04:59:09.426Z	21					Medium
tooltip_shoppingbox_close	1	www.naver.com	/	2025-04-17T08:33:41.879Z	26					Medium
'''

[line.split('\t') for line in c.splitlines()[1:]]

c = '''
ONID	710C1965A8271C8563AAA53A723454B4	www.naver.com	/	Session	42	✓				Medium
NID_AUT	AuEhaOvqGImKpFl0kLsdqFIdluZalVo4if074PfVfJFGV0DGWeDnoBkwlm91fuJZ	.naver.com	/	Session	71	✓	✓	Lax		Medium
NID_JKL	HLwiuJdVA958zWyDH3SaK67mcUj7knNdMSaZ06PB+dU=	.naver.com	/	Session	51		✓			Medium
NID_SES	AAABs3hWYHimoWXLskilSd12vI6+D71zGmwGePaMpl8xKBw4GEmhihw3sybyXmz43NxaCkZE8XjzvmGeRhjz6DDPUKMV6OGRB5D8xwophxJk3QqwK7GhB3H7YvQs8gAMpUaRJuPWB2wqTrx13+FQr9u+35ETHJyz9TkCPLrr7tk7M74Kd3DHp7tuZ08XLBpG5x7RJbsaGDbH//pup3gtGyTOzHWfzppy6dfp8oK9CSI0jivNeS0Y2BPhgznilzs+GpZPndDVAROi6AkHxNMNCtXB5aJnUFLydYjfZ2pO+6Ofb2wafmiGqqw006LSdesnVzc5MVkAjb3LopnWo010kELSDlrWrTLpbhqFXvip75gfAlflRnoRefTjXmHCW/CC11KpOpZP6iLyMHcZF2ztRvlLnQxYBwHS0xLRO7fxvPRLnzns5m0MP9Uxo32trXUVBCHlmUcT47+m+iRakgqd9IDNorJ0dg3vsi8S+BZ3+P638d85dpGHoFTu6UwNqspwTfVr4v3i1/+gHbGm7lbOZjqpan+XpUqQrFdcoRFtgra4RF9FxrwNcfL4DxVr55avmJuUi9pZ2mKpIapSZ7pewG9jKy4=	.naver.com	/	Session	611		✓	Lax		Medium
NM_srt_chzzk	1	www.naver.com	/	2024-03-24T08:08:14.000Z	13					Medium
NNB	63DRE2UT6DXWK	.naver.com	/	2025-04-27T08:08:24.608Z	16		✓	None		Medium
_ga	GA1.1.1302965497.1710648609	.naver.com	/	2025-04-26T05:43:01.944Z	30					Medium
_ga_3X9JZ731KT	GS1.1.1711086181.8.0.1711086187.0.0.0	.naver.com	/	2025-04-26T05:43:07.980Z	51					Medium
_gcl_au	1.1.697653695.1710648609	.naver.com	/	2024-06-15T04:10:09.000Z	31					Medium
nid_inf	573067207	.naver.com	/	Session	16					Medium
tooltip_paging_close	1	www.naver.com	/	2025-04-21T04:59:09.426Z	21					Medium
tooltip_shoppingbox_close	1	www.naver.com	/	2025-04-17T08:33:41.879Z	26					Medium
'''

for kv in [line.split('\t')[:2] for line in c.splitlines()[1:]]:
    sess.cookies.set(kv[0], kv[1])

sess.cookies



url = 'https://mail.naver.com'

resp = request('GET', url)
dom = BeautifulSoup(resp.text, 'html.parser')
dom.title

resp = request('GET', url, cookies=sess.cookies)
dom = BeautifulSoup(resp.text, 'html.parser')
dom.title

resp = sess.request('GET', url)
dom = BeautifulSoup(resp.text, 'html.parser')
dom.title

url = 'https://mail.naver.com/json/list'
params = {
    'folderSN':'-1',
    'page':1,
    'viewMode':'time',
    'previewMode':1,
    'sortField':1,
    'sortType':0,
    'u':'highs302'
}

resp = sess.request('POST', url, params=params)
resp.headers

resp.json().keys()

resp.json()['mailData'][0].keys()

resp.json()['mailData'][0]['subject']

for mail in resp.json()['mailData']:
    print(mail['subject'])

params['folderSN'] = 1 #페이지 수
resp = sess.request('POST', url, params=params)
for mail in resp.json()['mailData']:
    print(mail['subject'])

resp.request.headers

resp.request.headers['accept']

params['folderSN'] = 1
resp = sess.request('POST', url, params=params, headers={'accept':'application/json'})
for mail in resp.json()['mailData']:
    print(mail['subject'])

resp.headers['content-type']

# */* => text, plain
# application/json => application/json

resp.request.url, resp.request.body

from datetime import datetime

datetime.now()

dir(datetime.now())

datetime.now().timestamp()

datetime.now().microsecond



sess.cookies.clear()

url = 'https://www.instagram.com/'
resp = request('GET', url)
dom = BeautifulSoup(resp.text, 'html.parser')

dom.select('form')

dom

dom.body

# Commented out IPython magic to ensure Python compatibility.
# %%writefile instagram.json
# {
#     "id":"01045063891",
#     "pw":"sm07173!"
# }

with open('instagram.json', 'r', encoding='utf8') as fp:
    sns = load(fp)

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
params = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1710903436:AY5QAJ/zov84M/C/FHrzQFUuXZ1eegmb9agrXUDeGpwJDolZCmmDnU6+GD7JsLXb1RzMvbs8SJ11IXXUehtO90OcyeJGsv/ox39tCGtqFB+5xkO7y1rEiD40nS86HdOpvnMWlEMMGaUdPK6IVKXj',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': '01045063891'
}

resp = request('POST', url, data=params)
resp.status_code, resp.reason, resp.headers, resp.json()

resp.json()

# OAuth
#                           token
#                           -> key
# API:CSRF
# - callable service URI    -> 우리가 호출(CSRF)
# - callable service URI
# - callable service URI

url = 'https://www.instagram.com'
resp = request('GET', url)

resp.text

resp.headers

re.findall('csrf', resp.text, re.IGNORECASE)

resp.headers['set-cookie']

# csrftoken=vx12d41Ya3fp4m-f66Ksf- 중요

re.search(r'csrf_token":"(.+?)"', resp.text).group(1)

CSRF = re.search(r'csrf_token":"(.+?)"', resp.text).group(1)

headers = {
    'X-Csrftoken':CSRF
}

resp = request('POST', url, data=params, headers=headers)
resp.status_code, resp.reason, resp.headers

resp.request.headers

resp.text

url

params

# 암호화할 값 : AY5QAJ/zov84M/C/FHrzQFUuXZ1eegmb9agrXUDeGpwJDolZCmmDnU6+GD7JsLXb1RzMvbs8SJ11IXXUehtO90OcyeJGsv/ox39tCGtqFB+5xkO7y1rEiD40nS86HdOpvnMWlEMMGaUdPK6IVKXj

f'#PWD_INSTAGRAM_BROWSER:0:{None}:{sns["pw"]}'

from datetime import datetime
datetime.now().timestamp()

from datetime import datetime
int(datetime.now().timestamp())

t = int(datetime.now().timestamp())
params['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{t}:{sns["pw"]}'

resp = request('POST', url, data=params, headers=headers)
resp.status_code, resp.reason, resp.headers['content-type']

resp.request.headers

t = int(datetime.now().timestamp())
params['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{t}:{sns["pw"]}'

resp = request('POST', url, data=params, headers=headers, cookies={'csrftoken':CSRF})
resp.status_code, resp.reason, resp.headers['content-type']

url = 'https://www.instagram.com'
resp = request('GET', url)
CSRF = re.search(r'csrf_token":"(.+?)"', resp.text).group(1)

sess.request('GET', url)

t = int(datetime.now().timestamp())
params['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{t}:{sns["pw"]}'

resp = request('POST', url, data=params, headers=headers)
resp.status_code, resp.reason, resp.headers['content-type']

sess.cookies

resp.headers

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

t = int(datetime.now().timestamp())
params['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{t}:{sns["pw"]}'

resp = request('POST', url, data=params, headers=headers)
resp.status_code, resp.reason, resp.headers['content-type']

resp.json()



