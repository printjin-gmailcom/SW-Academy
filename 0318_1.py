# URLs
# PK HOST
# 1 네이버검색결과:www.naver.com
# 2 네이버블로그

# Links
# PK    LINK      Visited     Host.FK     inbound     REGDATE    Y/N
# 1   /search?q=수지             1            0
# 2   /id/30303                 2            1
# 3   /id/39393                 2            1
# 4   네이버블로그A-1               2           1
#     네이버블로그B-2               2           1
#       ...

# Links where Y/N='N' order by PK limit 0,N


# PR = inbound / 전체 link
# count(inbound = 1) => 1번 페이지가 갖는 전체 link의 수 = 4

# count() where inbound = 1 group by Host.FK => 1번 페이지로부터 inbound 그룹내 페이지 수 = 1
# URLs.host count(*)
# 네이버블로그     4

# count() where inbound = 1 => 1번 페이지로부터 inbound 페이지 수 = 1
# URLs.host count(*)
# 네이버블로그     4



# https://blog.naver.com/legal_clinic/223385997493
# https://blog.naver.com/legal_clinic/223386788669



import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()

cur.executescript('''
    CREATE TABLE URLs(
        PK INTEGER PRIMARY KEY,
        SCHEME TEXT NOT NULL DEFAULT 'http',
        NETLOC TEXT NOT NULL,
        REGDATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
''')

cur.execute('INSERT INTO URLs(NETLOC) VALUES("www.naver.com")')

cur.execute('SELECT * FROM URLs')
cur.fetchall()

cur.execute('DELETE FROM URLs')

cur.executescript('''
    DROP TABLE IF EXISTS URLs;
    CREATE TABLE URLs(
        PK INTEGER PRIMARY KEY,
        SCHEME TEXT NOT NULL DEFAULT 'http',
        NETLOC TEXT NOT NULL,
        REGDATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    DROP TABLE IF EXISTS Links;
    CREATE TABLE Links(
        PK INTEGER PRIMARY KEY,
        PATH TEXT NOT NULL DEFAULT '/',
        QS TEXT,
        FK INTEGER NOT NULL,
        REF INTEGER NOT NULL,
        VISITED INTEGER NOT NULL DEFAULT 0,
        REGDATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
''')

# FK INTEGER NOT NULL, # 어느 도메인에 속한 링크인지
# REF INTEGER NOT NULL, # 이전 도메인(outbound), inbound 링크의 출처
# VISITED INTEGER NOT NULL DEFAULT 0, # page 방문여부

from requests.compat import urlparse

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%88%98%EC%A7%80'
url_seg = urlparse(url)

cur.execute('SELECT PK FROM URLs WHERE NETLOC=?', (url_seg.netloc,))
temp = cur.fetchone()

if not temp:
    cur.execute('INSERT INTO URLs (SCHEME, NETLOC) VALUES(?,?)', url_seg[:2])

cur.execute('SELECT PK FROM URLs WHERE NETLOC=?', (url_seg.netloc,))
PK = cur.fetchone()[0]

cur.execute('SELECT * FROM URLs')
cur.fetchall

cur.execute('SELECT COUNT(PK) FROM Links WHERE FK=? AND PATH=?', (PK, url_seg.path))

if cur.fetchone()[0] == 0:
    cur.execute('INSERT INTO Links(PATH, QS, FK, REF) VALUES(?, ?, ?, 0)',
                (url_seg.path, url_seg.query, PK))
    con.commit()

cur.execute('SELECT * FROM Links')
cur.fetchall

from requests.compat import urlunparse, urljoin
from requests import get
from bs4 import BeautifulSoup
import re

while True:
    # ASC => Queue, 10개의 페이지만 수집
    cur.execute('''
        SELECT A.PK, B.PK, B.FK, B.REF, A.SCHEME, A.NETLOC, B.PATH, B.QS FROM URLs AS A
        INNER JOIN Links AS B
        ON B.FK = A.PK
        WHERE B.VISITED=0
        ORDER BY B.REGDATE ASC
        LIMIT 0, 10
    ''')
#     A.PK => 어느 사이트로부터 왔는가
#     B.PK => 수집했는지 여부 UPDATE
#     B.FK => ?
    urls = cur.fetchall()

    if len(urls) == 0:
        break

    while urls:
        url_seg = urls.pop(0)
        url = urlunparse((url_seg[4], url_seg[5], url_seg[6], None,
                          url_seg[7], None))

        resp = get(url)
        cur.execute('UPDATE Links SET VISITED=1 WHERE PK=?', (url_seg[1],))
        con.commit()

        if resp.status_code == 200 and\
           re.search(r'text\/html', resp.headers['content-type']):
            dom = BeautifulSoup(resp.text)
            for tag in dom.select('a[href], iframe[src]'):
                link = tag.attrs['href' if tag.has_attr('href') else 'src']
                newLink = urljoin(url, link)

                if re.match(r'javascript|data|mailto', newLink):
                    continue

                newlink_seg = urlparse(newLink)
                cur.execute('SELECT PK FROM URLs WHERE NETLOC=?',
                            (newlink_seg.netloc,))
                temp = cur.fetchone()

                if not temp:
                    cur.execute('INSERT INTO URLs (SCHEME, NETLOC) VALUES(?,?)',
                                newlink_seg[:2])

                cur.execute('SELECT PK FROM URLs WHERE NETLOC=?',
                            (newlink_seg.netloc,))
                PK = cur.fetchone()[0]

                cur.execute('SELECT COUNT(PK) FROM Links WHERE FK=? AND PATH=?',
                            (PK, newlink_seg.path))

                if cur.fetchone()[0] == 0:
                    cur.execute('INSERT INTO Links(PATH, QS, FK, REF) VALUES(?, ?, ?, ?)',
                                (newlink_seg.path, newlink_seg.query, PK, url_seg[0]))
                    con.commit()

cur.execute('SELECT * FROM Links WHERE VISITED=1')
len(cur.fetchall()) # => Visited

cur.execute('SELECT * FROM Links WHERE VISITED=0')
len(cur.fetchall()) # => URLs

# A
cur.execute('''
    SELECT COUNT(*) FROM Links WHERE REF=1
''')
cur.fetchone()[0] # 1번 도메인의 outbound link의 수

# B
cur.execute('''
    SELECT FK, COUNT(*) FROM Links WHERE REF=1 GROUP BY FK
''')
# 1번 도메인의 outbound를 도메인별로 구분한 수(도메인 입장; inbound)
for page, inboun in cur.fetchall():
    print(page, inboun/127) # 정규화

# d = .85
# PR(B) == (1-d) + d*(B/A)
#          .15  + .85 = [0~1] => P

con.close()



from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Text
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///:memory:', echo = True)

base = declarative_base()

class User(base):
    __tablename__ = 'T_USER'
    __table_args__ = {'extend_existing':True}

    pk = Column('PK', Integer, primary_key = True)
    name = Column('NAME', Text, nullable=False)

    def __repr__ (self):
        return f'pk={self.pk}, name={self.name}'

# BASE USER CLASS

# ORM TABLE 객체

base.metadata.tables

# TABLE 객체를 db에 반영

base.metadata.create_all(engine)

# Mappting;base     ORM;core      DB
# declarative-base  Metadata     RBDMS
# Class(base)       Table 객체   Table 생김

a = User(name='아무개')

a

session = sessionmaker(engine)
sess =  session()

sess.add(a)

sess.dirty

sess.is_modified(a)

sess.commit()

sess.is_modified(a)

a

a.pk

a.name = '이름바뀜'

a

sess.dirty

sess.commit()

sess.query(User).all()

sess.query(User).all()[0] is a

sess.query(User).filter(User.pk == 1).all()[0] is a

type(sess.query(User).all()[0])

sess.query(User).all()[0].pk

base.registry.dispose()

sess.query(User).all()[0].pk

base.metadata.tables

class User(base):
    __table__ = base.metadata.tables['T_USER']

sess.query(User).all()[0]

from sqlalchemy.schema import Table

class User(base):
    __table__ = Table('T_USER', base.metadata, reflect=True)
    __table_args__ = {'extend_existing':True}

class Address(base):
    __tablename__ = 'T_ADDRESS'
    __table_args__ = {'extend_existing':True}

    pk = Column('PK', Integer, primary_key=True)
    address = Column('ADDRESS', Text)
    fk = ForeignKey(User.PK)

base.metadata.create_all(engine)

a = sess.query(User).one()

address = Address(address='주소1', fk=a.PK)

address.fk

sess.add(address)

sess.dirty

sess.is_modified(address)

sess.commit()

sess.close()

engine.dispose()



base = declarative_base()
engine= create_engine('sqlite:///:memory:')

class User(base):
    __tablename__ = 'T_USER'

    pk = Column('PK', Integer, primary_key=True)
    name = Column('NAME', Text, nullable=False)

class Address(base):
    __tablename__ = 'T_ADDRESS'

    pk = Column('PK', Integer, primary_key=True)
    address = Column('NAME', Text, nullable=False)
    fk = Column('FK', Integer, nullable=False)

base.metadata.create_all(engine)

session = sessionmaker(engine)
sess = session()

sess.add(User(name='이름1'))

a = sess.query(User).one()

sess.add(Address(address='주소1', fk=a.pk))

sess.query(Address).all()[0].fk

from sqlalchemy.sql import join

sess.query(User.name, Address.address).\
select_from(join(User, Address, User.pk==Address.fk)).all()

class Phone(base):
    __tablename__ = 'T_PHONE'

    pk = Column('PK', Integer, primary_key = True)
    phone = Column('PHONE', Text)
    fk = ForeignKey(User.pk)

base.metadata.create_all(engine)

sess.add(Phone(phone='전화번호', fk=a.pk))
sess.commit()

sess.close()
base.metadata.clear()
engine.dispose()

engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(engine)
sess = session()

base = declarative_base()

class User(base):
    __tablename__ = 'T_USER'

    pk = Column('PK', Integer, primary_key=True)
    name = Column('NAME', Text, nullable=False)

class Address(base):
    __tablename__ = 'T_ADDRESS'

    pk = Column('PK', Integer, primary_key=True)
    address = Column('NAME', Text, nullable=False)
    fk = Column('FK', Integer, ForeignKey(User.pk))

base.metadata.create_all(engine)

a = User(name='이름1')
sess.add(a)
sess.commit()

sess.add(Address(address='주소1', fk=a.pk))
sess.commit()

sess.query(User.name, Address.address).join(Address).all()

#                                   declartive_base
#                     base.metadata.table       base.registry
#                     base.metadata.clear()     base.registry.dispose()
# Databse             ORM-CORE                  ORM:mapper
# T_USER              Table('T_USER')           User(base)
# T_ADDRESS           Table('T_ADDRESS')        Address(base)
#                                               Relationship
# <=================== session(engine) =====================>
# join(T, T, on = Reference/ForiegnKey X)
# Left join(Right on생략).join(A).join(B)

base.metadata.clear()
base.metadata.tables

base.metadata.reflect(engine)
base.metadata.tables

base.metadata.tables['T_ADDRESS']

# User.addresses[0] = 주소

sess.close()
base.registry.dispose()
base.metadata.clear()
engine.dispose()

engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(engine)
sess = session()

# class Artist(base):
#     __tablename__ = 'T_ARTIST'
#     __table_args__ = {'extend_existing':True} # 수정 class 덮어씌우는

#     pk = Column('PK', Integer, primary_key=True)
#     name = Column('NAME', Text)
#     albums = relationship('Album', back_populates='artist', uselist=True) # 어느 class

#     def addAlbum(self, s, name):
#         a = s.query(Artist).filter(Artist.pk==self.pk).one()
#         a.albums.append(Album(name=name))
#         s.commit()

#     def delAlbum(self, s, name):
#         a = s.query(Artist).filter(Artist.pk==self.pk).one()
#         list(filter(lambda r:r.name==name, self.albums))[0]
#         a.albums.remove(list(filter(r:r.name==name, self.albums))[0])
#         a.commit()

#     def __repr__(self):
#         return f'pk={self.pk}, name={self.name}'

# class Album(base):
#     __tablename__ = 'T_ALBUM'
#     __table_args__ = {'extend_existing':True}

#     pk = Column('PK', Integer, primary_key=True)
#     name = Column('NAME', Text)
#     fk = Column('FK', None, ForeignKey(Artist.pk))
#     artist = relationship('Artist', back_populates='albums', uselist=False)

#     def __repr__(self):
#         return f'pk={self.pk}, name={self.name}'

from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

base = declarative_base()

class Artist(base):
    __tablename__ = 'T_ARTIST'
    __table_args__ = {'extend_existing': True}

    pk = Column('PK', Integer, primary_key=True)
    name = Column('NAME', Text)
    albums = relationship('Album', back_populates='artist')

    def addAlbum(self, session, name):
        self.albums.append(Album(name=name))
        session.commit()

    def delAlbum(self, session, name):
        album_to_delete = next((album for album in self.albums if album.name == name), None)
        if album_to_delete:
            self.albums.remove(album_to_delete)
            session.commit()

    def __repr__(self):
        return f'pk={self.pk}, name={self.name}'

class Album(base):
    __tablename__ = 'T_ALBUM'
    __table_args__ = {'extend_existing': True}

    pk = Column('PK', Integer, primary_key=True)
    name = Column('NAME', Text)
    fk = Column('FK', Integer, ForeignKey('T_ARTIST.PK'))
    artist = relationship('Artist', back_populates='albums')

    def __repr__(self):
        return f'pk={self.pk}, name={self.name}'

base.metadata.create_all(engine)

Artist(name='아무개')

sess.add(Artist(name='아무개'))
sess.commit()

a = sess.query(Artist).one()

sess.dirty, sess.is_modified(a)

a.albums.append(Album(name='가수1의 앨범1'))

sess.dirty, sess.is_modified(a)

sess.commit()

a.albums[0] is sess.query(Album).one()

sess.query(Album).one().artist

from sqlalchemy.orm import relationship



