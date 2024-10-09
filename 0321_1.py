# Crawling + Scraping

# [주의사항]
# 1. robots.txt
# 2. 과도한 트래픽 X
# 3. 저작권(DB)
# 4. 이용약관 => API
# 5. 개인정보 => API

# [기본개념]
# HTTP => Request / Response 쌍
#         Header / Body(*)
#         ------
# Request status_code, reason, content-type, set-cookie, user-agent...
#         Referer, X-..., UUID, ...
#         POST/PUT... body => paramsKey=paramsValue&... (Bytes)
#         GET / POST => params 주소, 바디? request.body 쓰느냐 차이
# Response Body => content-type
#                  text/plain, html, application/json,xml,javascript...
#                  image/*, ...
#                  text=>str객체, html=>dom, xml=>dom
#                  json=>json, MIME=>bytes
# Session(Cookie) | Cookie의 저장소 Client(Key, Value, Domain, Path, ...)
# Crawler => HyperLink를 끊임없이 탐험, Focused Crawling
# Scraper => 특정 페이지, 특정 요소(데이터) 추출
# DHTML(AJAX-XHR) => DOM 생성되는 시점 최초에만, 그 이후에는 data(*)
#                 => Javascript Engine(Phantom JS => Selenium.Chrome)



from requests.sessions import Session
from requests import request
from bs4 import BeautifulSoup
from datetime import datetime
import re

# 시크릿탭(창)으로 실행

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
data = {
    'enc_password': None,
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': '01045063891'
}

encpw = ['#PWD_INSTAGRAM_BROWSER', '0', str(int(datetime.now().timestamp())), 'smj07173!']
data['enc_password'] = ':'.join(encpw)

resp = request('POST', url, data=data)
resp.text

#          g              c      b            a
#PWD_INSTAGRAM_BROWSER:10:1711100338:AVlQAIMponJ4xiw0SSbcLA0UOfmSfdVfvNQtQFGvIJKTTl1dkzzJbX4+3pTesJ9Rn7YCDGZk2v+pJmoh2kxIoOoGyX0AXEPl3bEvNICm/W1l16bRvUFSp3bUh6tb3a9fdA1maUBp+GgYteGsbA==
# [g, c, b, a].join(":")
# g => enc 어느 옵션
# c => enc 옵션 값
# b => 시간
# a => 암호

# encpw = ['#PWD_INSTAGRAM_BROWSER', '0', str(int(datetime.now().timestamp())), 'smj07173!']
#                                 PLAINTEXT,                                      비밀번호

url = 'https://www.instagram.com/'

resp = request('GET', url)
csrf = re.search(r'csrf_token":"(.+?)"', resp.text).group(1)
csrf

url = 'https://www.instagram.com/'

resp = request('GET', url)
csrf = re.search(r'csrf_token":"(.+?)"', resp.text).group(1)
header = {
    'x-csrftoken':csrf
}

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
data = {
    'enc_password': None,
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': '01045063891'
}

encpw = ['#PWD_INSTAGRAM_BROWSER', '0', str(int(datetime.now().timestamp())), 'smj07173!']
data['enc_password'] = ':'.join(encpw)

resp = request('POST', url, data=data, headers=header)
resp.text

# app_id : 936619743392459



url = 'https://www.instagram.com/'

s = Session()
resp = s.request('GET', url)
csrf = re.search(r'csrf_token":"(.+?)"', resp.text).group(1)
header = {
    'x-csrftoken':csrf
}

url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
data = {
    'enc_password': None,
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': '01045063891'
}

encpw = ['#PWD_INSTAGRAM_BROWSER', '0', str(int(datetime.now().timestamp())), 'smj07173!']
data['enc_password'] = ':'.join(encpw)



resp = s.request('POST', url, data=data, headers=header)
resp.text

s.cookies.get('csrftoken')

header['x-csrftoken']



!pip install selenium

# install chrome driver > exe 실행 하는 것 아님

!pip install chromedriver_autoinstaller

from selenium.webdriver import Chrome, ChromeOptions

driver = Chrome()

opts = ChromeOptions()
# headless - 빠른데 user-agent 가 달라짐. 가끔 튕기는 사이트도 있음.

driver # 브라우저의 고유값 - session

driver.get('https://www.naver.com')

driver.page_source

# driver.page_source != request.text
#     dom                    raw

dom = BeautifulSoup(driver.page_source, 'html.parser')

from selenium.webdriver.common.by import By

# By.CSS_SELECTOR = bs4.select
# By.CLASS_NAME = bs4.find~(attr={'calss':})
# By.ID = bs4.find~(attr={'id':})
# By.LINK_TEXT = bs4.find~('a', string='')
# By.NAME = bs4.find~(attrs={'name':})
# By.TAG_NAME = bs4.find~('태그이름')
# By.XPATH

# diver.find_element = find
# diver.find_elements = find_all
driver.find_element(By.TAG_NAME, 'form')

driver.find_element(By.CSS_SELECTOR, 'form')

driver.find_elements(By.CSS_SELECTOR, 'form > input')

# ., .., /, //, [@속성=""]
driver.find_element(By.XPATH, 'form')

driver.find_element(By.XPATH, 'body')

driver.find_element(By.XPATH, '/html')

driver.find_element(By.XPATH, '/html/head')

driver.find_element(By.XPATH, '/head')

driver.find_element(By.XPATH, '//head')

len(driver.find_elements(By.XPATH, '//form'))

for node in driver.find_elements(By.XPATH, '//form//input'):
    print(node.tag_name, node.get_attribute('name'), node.get_attribute('value'))

driver.find_element(By.XPATH, '//form//input[@name="id"]')

driver.find_element(By.XPATH, '//form//input[@name="pw"]')

uid = driver.find_element(By.XPATH, '//form//input[@name="id"]')
upw = driver.find_element(By.XPATH, '//form//input[@name="pw"]')

uid.click()

type(uid), type(uid.click())

dir(uid)

# uid.send_keys('내아이디')
# upw.send_keys('비밀번호')
# => captcha => clipboard

from selenium.webdriver.common.keys import Keys

uid.clear()
upw.clear()
uid.send_keys('highs302')
upw.send_keys('@naver07173')

driver.find_element(By.XPATH, '//form//button[@type="submit"]').click()

driver.get('https://mail.naver.com')

for node in driver.find_elements(By.XPATH, '//a[@class="mail_title_link"]'):
    print(node.text)
    print(node.get_attribute('href'))

driver.find_elements(By.XPATH, '//a[@class="mail_title_link"]')[0]

driver.find_elements(By.XPATH, '//a[@class="mail_title_link"]')[0].click()

driver.find_element(By.XPATH, '/html').send_keys(Keys.BACKSPACE)

driver.execute_script('history.back()')

driver.execute_script('console.log(history)')

driver.find_elements(By.XPATH, '//a[@class="mail_title_link"]')[0].text

item = driver.find_elements(By.XPATH, '//a[@class="mail_title_link"]')[0]

item.find_elements(By.XPATH, '//a[@class="mail_title_link"]')

item.find_elements(By.XPATH, './/a[@class="mail_title_link"]')

item.find_elements(By.XPATH, '../..//a[@class="mail_title_link"]')

item.find_elements(By.XPATH, '../../../../..//a[@class="mail_title_link"]')

driver.find_elements(By.CSS_SELECTOR, 'a.mail_title_link')

item.is_displayed(), item.is_enabled(), item.is_selected()
# -> 화면에도 보이는지(*) -> a, btn disabled -> select option



driver.get('https://lms.sunde41.net')

from json import load

with open('./lms.json', 'r') as fp:
    lms = load(fp)

driver.find_elements(By.CSS_SELECTOR, 'form')

driver.find_elements(By.XPATH, '//form//input')

for node in driver.find_elements(By.XPATH, '//form//input'):
    print(node.get_attribute('name'))

email = driver.find_element(By.XPATH, '//form//input[@name="email"]')
password = driver.find_element(By.XPATH, '//form//input[@name="password"]')

email.clear()
password.clear()
email.send_keys(lms['printjin@gmail.com'])
password.send_keys(lms['@01045063891'])

driver.find_element(By.XPATH, '//form//*[@type="submit"]').click()

for ul in driver.find_elements(By.XPATH, '//ul[@class="navbar-nav"]'):
    for li in ul.find_elements(By.XPATH, './li'):
        print(li.text)
    print()

driver.find_element(By.XPATH, '//ul[@class="navbar-nav"]/li').click()

for node in driver.find_elements(By.XPATH, '//table[@id="lesson"]//div[@class="dropdown"]'):
    print(node.tag_name)

for node in driver.find_elements(By.XPATH, '//table[@id="lesson"]//div[@class="dropdown"]'):
    print(node.text)

for node in driver.find_elements(By.XPATH, '//table[@id="lesson"]//div[@class="dropdown"]'):
    a = node.find_element(By.CSS_SELECTOR, 'a.dropdown-toggle')
    link = node.find_element(By.CSS_SELECTOR, 'a.dropdown-toggle + .dropdown-menu')

    if not link.is_displayed():
        a.click()

    print(node.text, node.is_displayed(), link.is_displayed())

    a.click()



dom = BeautifulSoup(driver.page_source, 'html.parser')

dom.select('#lesson a.dropdown-item')

# wait != sleep()
# explicit_wait => 누군가(명확히 대상)가 어떤 이벤트(오류)가 사라질때까지 기다리는것
# implicit_wait => 암묵적으로 기다리는 것

driver.implicitly_wait = 10

for node in driver.find_elements(By.XPATH, '//table[@id="lesson"]//div[@class="dropdown"]'):
    a = node.find_element(By.CSS_SELECTOR, 'a.dropdown-toggle')
    link = node.find_element(By.CSS_SELECTOR, 'a.dropdown-toggle + .dropdown-menu')


    print(node.text, node.is_displayed(), link.is_displayed())
    link.click()
    a.click()
    break

from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver, 10, 0.5, [element_to_be_clickable])

a = driver.find_element(By.CSS_SELECTOR, 'a.dropdown-toggle + .dropdown-menu')
wait.until((a))

