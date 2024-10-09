 #    (1)        (2)        (3)
 #   RDBMS      ORM-Core    ORM
 #        ------  Meta  ----
 #        engine      declrative_base
 #    connect dialect
 #        session
 # 물리적 Table    Table객체   Class객체
 #  database    meta.tables   base
 #                           User, User, User, ..., User.pk
 #                ------------------
 #                     # Mapper[:namespace]





from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Text
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(engine)
sess = session()

base = declarative_base()

class Artist(base):
    __tablename__ = 'T_ARTIST'

    pk = Column('PK', Integer, primary_key=True)
    name = Column('NAME', Text)

class Album(base):
    __tablename__ = 'T_ALBUM'

    pk = Column('PK', Integer, primary_key=True)
    name = Column('NAME', Text)
    fk = Column('FK', ForeignKey(Artist.pk))

base.metadata.create_all(engine)

a = Artist(name='수지')

sess.add(a)
sess.commit()

sess.add(Album(name='수지앨범', fk=a.pk))
sess.commit()

sess.query(Artist).join(Album).all()

del base
base = declarative_base()
base.metadata.reflect(engine)

class Artist(base):
    __table__ = base.metadata.tables['T_ARTIST']

    pk = base.metadata.tables['T_ARTIST'].c.PK
    name = base.metadata.tables['T_ARTIST'].c.NAME
    albums = relationship('Album', back_populates='artist', uselist=True)

class Album(base):
    __table__ = base.metadata.tables['T_ALBUM']

    pk = base.metadata.tables['T_ALBUM'].c.PK
    name = base.metadata.tables['T_ALBUM'].c.NAME
    fk = base.metadata.tables['T_ALBUM'].c.FK
    artist = relationship('Artist', back_populates='albums', uselist=False)

a = sess.query(Artist).all()[0]

a.albums[0].name

a.albums.append(Album(name='수지앨범2', fk=a.pk))

sess.dirty, sess.is_modified(a)

sess.commit()

len(a.albums), a.albums[-1].name

del base
base = declarative_base()
base.metadata.reflect(engine)

class Artist(base):
    __table__ = base.metadata.tables['T_ARTIST']
    __table_args__ = {'extend_existing':True}

    pk = base.metadata.tables['T_ARTIST'].c.PK
    name = base.metadata.tables['T_ARTIST'].c.NAME
    albums = relationship('Album', back_populates='artist', uselist=True)

    def addAlbum(self, s, name):
        s.add(Album(name=name, fk=self.pk))
        s.commit()

    def delAlbum(self, s, name):
#         album = s.query(Album).filter(Album.name==name).one()
        album = list(filter(lambda a:a.name == name, self.albums))[0]
        self.albums.remove(album)
        s.commit()

class Album(base):
    __table__ = base.metadata.tables['T_ALBUM']
    __table_args__ = {'extend_existing':True}

    pk = base.metadata.tables['T_ALBUM'].c.PK
    name = base.metadata.tables['T_ALBUM'].c.NAME
    fk = base.metadata.tables['T_ALBUM'].c.FK
    artist = relationship('Artist', back_populates='albums', uselist=False)

a = sess.query(Artist).all()[0]

a.addAlbum(sess, '수지앨범3')

len(a.albums), a.albums[-1].name

a.delAlbum(sess, '수지앨범3')

len(a.albums), a.albums[-1].name



# 포스팅           +      해시태그   (반드시 풀에 존재)
#                         +1 -1
#  Post                  Hashtag
# Post.addTags     Tag.plus(), Tag_minus()

# M(Model)VC, M(Model)VVM



from requests import request

url = 'https://www.ppomppu.co.kr/zboard/zboard.php'
params = {
    'id':'freeboard',
    'page':1
}

resp = request('GET', url, params=params)

resp.headers['content-type']

resp.text.encode('euc-kr').decode('utf8', errors='ignore')

resp.content.decode('utf8', errors='ignore')

# resp.content == resp.text.encode('euc-kr')

from bs4 import BeautifulSoup

dom = BeautifulSoup(resp.text, 'html.parser')

len(dom.select('#revolution_main_table tbody > tr:first-child ~ tr > td:nth-child(3)'))

len(dom.select('#revolution_main_table tr#headNotice ~ tr > td:nth-child(3)'))

for tag in dom.select('#revolution_main_table tr#headNotice ~ tr > td:nth-child(3)'):
    print(tag.get_text())

for tag in dom.select('#revolution_main_table tr#headNotice ~ tr > td:nth-child(3)'):
    print(tag)

for tag in dom.select('#headNotice ~ tr > td:nth-child(3) > a'):
    print(tag.attrs['href'])

from  requests.compat import urljoin

for tag in dom.select('#headNotice ~ tr > td:nth-child(3) > a'):
    print(urljoin(url, tag.attrs['href']))

resp = request('GET', 'https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=1623&no=8711414')

resp.headers['content-type']

dom = BeautifulSoup(resp.text, 'html.parser')

dom.select_one('.board-contents')

dom

dom.select_one('.han')

dom.select_one('.pic_bg tr > .han')

dom.select_one('table table table > tr:first-child> :first-child')

url = 'https://pythonscraping.com/pages/javascript/ajaxDemo.html'
resp = request('GET', url)

print(resp.text)

url = 'https://pythonscraping.com/pages/javascript/ajaxDemo.html'
resp = request('GET', url)

dom = BeautifulSoup(resp.text, 'html.parser')

dom.body.script

import re

re.search(r'^\s*url\s*:\s*[\'\"]?(.+?)[\'\"]?,?$',
          dom.body.script.text, re.MULTILINE).group(1)



url = 'https://brunch.co.kr/search?q=수지'
resp = request('GET', url)
dom = BeautifulSoup(resp.text, 'html.parser')

dom.find_all(string=re.compile('수지'))

dom.select('form[action]')

dom.select('form[action]')[0]

dom.select('form[action] input[name]')[0]

for tag in dom.select('form[action] input[name]'):
    print(tag.attrs['name'], tag.attrs['value'])

url = 'https://api.brunch.co.kr/v1/search/article'
params = {
    'q' : '수지',
    'page' : 1,
    'pagesize' : 20,
    'highlighter' : 'y',
    'escape' : 'y',
    'sortBy' : 'accu'
}

resp = request('GET', url, params=params)

resp.status_code, resp.reason, resp.headers, resp.request.headers

for it in resp.json()['data']['list']:
    print(it['title'])

url = 'https://api.brunch.co.kr/v1/search/article'
params = {
    'q' : '수지',
    'page' : 1,
    'pagesize' : 20,
    'highlighter' : 'n',
    'escape' : 'y',
    'sortBy' : 'accu'
}

resp = request('GET', url, params=params)

for it in resp.json()['data']['list']:
    print(it['title'])

url = 'https://api.brunch.co.kr/v1/search/article'
params = {
    'q' : '수지',
    'page' : 1,
    'pagesize' : 20,
    'highlighter' : 'n',
    'escape' : 'n',
    'sortBy' : 'accu'
}

resp = request('GET', url, params=params)

for it in resp.json()['data']['list']:
    print(it['title'])

url = 'https://api.brunch.co.kr/v1/search/article'
params = {
    'q' : '수지',
    'page' : 1,
    'pagesize' : 20,
    'highlighter' : 'n',
    'escape' : 'n',
    'sortBy' : 'recency'
}

resp = request('GET', url, params=params)

for it in resp.json()['data']['list']:
    print(it['title'])

url = 'https://brunch.co.kr/'
resp = request('GET', url)
dom= BeautifulSoup(resp.text, 'html.parser')

dom.select('form')

url = 'https://api.brunch.co.kr/v1/search/live/'

params = {
    'q':'수지'
}
resp = request('GET', url, params=params)
resp.status_code, resp.headers['content-type']

list(map(lambda r:r['title'], resp.json()['data']['article']))

url = 'https://ac.search.naver.com/nx/ac'

params = {
    'q':'수지',
    'con':'0',
    'frm':'nv',
    'ans':'2',
    'r_format':'json',
    'r_enc':'UTF-8',
    'r_unicode':'0',
    't_koreng':'1',
    'run':'2',
    'rev':'4',
    'q_enc':'UTF-8',
    'st':'100',
}
resp = request('GET', url, params=params)
resp.status_code, resp.headers

resp.json()

resp.json().items()

resp.json().keys()

url = 'https://comic.naver.com/api/webtoon/titlelist/weekday'

params = {
    'week':'tue',
    'order':'user'
}
resp = request('GET', url, params=params)
resp.status_code, resp.headers

url = 'https://comic.naver.com/api/webtoon/titlelist/weekday'

params = {
    'week':'mon',
    'order':'user'
}
resp = request('GET', url, params=params)
resp.status_code, resp.headers

params['week'] = 'wed'
resp = request('GET', url, params=params)
resp.status_code, resp.headers

params['week'] = 'tue'
resp = request('GET', url, params=params)
resp.status_code, resp.headers

resp.json()['titleList'][0]

resp.json()['titleList'][0].keys()

# https://comic.naver.com/webtoon/list?titleId=814543&tab=tue

for node in resp.json()['titleList']:
    print(node['titleId'], node['titleName'])

wurl = 'https://comic.naver.com/webtoon/list?titleId={}&tab={params["week"]}'''

wurl

wurl = 'https://comic.naver.com/webtoon/list?titleId={}&tab={}'.format(resp.json()['titleList'][2]['titleId'], params["week"])

wurl

url2 = 'https://comic.naver.com/api/article/list?titleId=814543&page=1'
resp = request('GET', url2)
resp.headers['content-type']

resp.json()['articleList'][0]

url = 'https://comic.naver.com/webtoon/detail?titleId=814543&no=32&week=tue'
resp = request('GET', url)
resp.headers['content-type']

dom = BeautifulSoup(resp.text, 'html.parser')

dom.select('#sectionContWide > img[src]')



def webtoonList(week):
    url = 'https://comic.naver.com/api/webtoon/titlelist/weekday'
    params = {
        'week':week,
        'order':'user'
    }

    resp = request('GET', url, params=params)

    if resp.status_code == 200 and\
       re.search(r'application\/json', resp.headers['content-type']):
        return resp.json()

    return None

def findByName(title, wl):
    result = dict()
    for item in list(filter(lambda r:re.search(title, r['titleName']),
                            wl['titleList'])):
        result[item['titleId']] = item['titleName']
    return result

findByName('마음의', webtoonList('tue'))

def webtoonNo(tid, page=1):
    url = 'https://comic.naver.com/api/article/list'
    params = {
        'titleId':tid,
        'page':page
    }

    resp = request('GET', url, params=params)

    if resp.status_code == 200 and\
       re.search(r'application\/json', resp.headers['content-type']):
        return list(map(lambda r:{r['no']:r['subtitle']},
                        resp.json()['articleList']))

    return None

webtoonNo(814543)

def imgDownloader(tid, no):
    url = 'https://comic.naver.com/webtoon/detail'
    params = {
        'titleId':tid,
        'no':no
    }

    resp = request('GET', url, params=params)

    if resp.status_code == 200 and\
       re.search(r'text\/html', resp.headers['content-type']):
        dom = BeautifulSoup(resp.text, 'html.parser')
        return list(map(lambda r:urljoin(resp.request.url, r.attrs['src']),
                        dom.select('#sectionContWide > img[src]')))

    return None

imgDownloader(814543, 32)



from os import mkdir, listdir

if '0319' in listdir('.'):
    mkdir('./0319')



url = 'https://pythonscraping.com/pages/login.html'

resp = request('GET', url)
resp.text

# GET : 주소에다 파라미터 [과거]?id=내아이디&pw=내비밀번호
# 로그인 (정보 기입) -> 서버로 요청
# POST : HTTP.Request.Body = id=내아이디&pw=내비밀번호

dom = BeautifulSoup(resp.text, 'html.parser')
for tag in dom.select('form input[name]'):
    print(tag['name'])

dom = BeautifulSoup(resp.text, 'html.parser')
for tag in dom.select('form input[name]'):
    print(tag['name'])
form = dom.select_one('form')
form.attrs['action'], form.attrs['method']

urljoin(url, form.attrs['action'])

params = {
    'username' : '아무개',
    'password' : 'password'
}

resp = request('POST', urljoin(url, form.attrs['action']), data = params)
resp.status_code

resp.request.body

resp.headers

# cookies, session



