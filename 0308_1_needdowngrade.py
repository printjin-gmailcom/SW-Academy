# 데이터관리에는 orm 사용 자제, 오버헤드때문에 게속 속도가 느려짐.
# orm은 프로그래밍 테크닉 sqlqlchemy, diango 등의 종류가 있음



import sqlalchemy # 설치 필요

sqlalchemy.__version__

!pip install sqlalchemy

from sqlalchemy.engine import create_engine
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, Text
from sqlalchemy.sql import select, insert, update

!dir *.db

import os
os.system('dir *.db')

engine = create_engine('sqlite:///orm.db', echo = True) #에코옵션 : 어떻게 작업하는지 보여줌

#    1           2              3            4
# python       orm           rdbbms       databse
#              core          sqlite       file
#        obj           sql
#  (class->MetaData)



from sqlalchemy.schema import MetaData

MetaData()

meta = MetaData()

meta.tables

meta.clear()

# 엔진통해서 연결뿐

# Table("테이블이름", "어딘가에 등록, 메타데이터", )
# Column("확인할거다수존재")

pk = Column('PK', Integer, primary_key = True)

Table('User', meta,
      Column('PK', Integer, primary_key=True),
      Column('NAME', Text, nullable=False))

meta.tables

meta.create_all(engine)

import os
os.system('dir *.db')

!dir *.db

meta.tables['User']

User = meta.tables['User']

print(select(User)), print(User.select())



# sql 20 ver 에서는 적동하지 않음. 1.4ver로 낮춰서 작동 실행 필요.

rst = engine.execute(select(User))

rst.fetchall()

type(rst)

print(insert(User)) # 해당 테이블에 해당되는 전체 아무것도 안함. 파라미터 요구
print(insert(User).values(NAME='어쩌고')) # 특정 요구하니까 컬럼의 변화 발생
print(insert(User).values(NAME='어쩌고').compile().params) # 들어갔는지 확인

engine.execute(insert(User).values(NAME='어쩌고'))

userList = engine.execute(select(User)).fatchall()

userList[0]

for person in ['사람1', '사람2', '사람3']:
    engine.execute(User.insert().values(NAME=person))

from sqlalchemy.sql import or_, and_

print(meta.tables['User'].c['PK'] == 1)
print(User.columns.PK == 2 or User.columns.PK == 3)
print(or_(User.columns.PK == 2, User.columns.PK == 3))

print(select(User).where(User.c['PK'] == 1))
print(select(User).where(User.c['PK'] == 1).compile().params)

engine.execute(User.select().where(User.c['PK'] == 1)).fetchall()
engine.execute(User.select().where(or_(User.c['PK'] == 1, User.c['PK'] == 2))).fetchall()

dir(User.select().order_by(User.c['PK'])

# meta.drop_all()
meta.clear()

meta.reflect(engine)

print(meta.tables['User'].select())

Table('Info', meta,
      Column('PK', Integer, primary_key=True),
      Column('EMAIL', Text, nullable=False))

# Meta         ORM          RDBMS
#                           User
# User
# Info
#              --->          Info

meta.create_all(engine, [meta.tables['Info']])



from sqlalchemy.schema import ForeignKey

Table('Info2', meta,
      Column('PK', Integer, primary_key=True),
      Column('NAME', Text),
      Column('FK', Text, nullable=False))

Table('Info3', meta,
      Column('PK', Integer, primary_key=True),
      Column('NAME', Text),
      Column('FK', Text, ForeignKey(meta.tables['User'].c['PK'])))

# join on절

meta.tables.keys()

meta.create_all(engine)



engine.execute(User.select()).fetchall()

meta.tables['Info2'].insert().values(NAME='어쩌고 정보', FK=1)

meta.tables['Info3'].insert().values(NAME='어쩌고 정보', FK=1)

engine.execute(meta.tables['Info2'].insert().values(NAME='어쩌고 정보', FK=1))

engine.execute(meta.tables['Info3'].insert().values(NAME='어쩌고 정보', FK=1))



from sqlalchemy.sql import join

print(join(meta.tables['User'], meta.tables['Info2'],
      meta.tables['User'].c['PK']==meta.tables['Info2'].c['FK']))

# foreign key => on절 을 만들어줘야함

print(join(meta.tables['User'], meta.tables['Info3']))

print(select(meta.tables['User'].c['PK'], meta).select_from(
        join(meta.tables['User'], meta.tables['Info2'],
             meta.tables['User'].c['PK']==meta.tables['Info2'].c['FK'])))

User = meta.tables['User']
Info2 = meta.tables['Info2']
Info3 = meta.tables['Info3']

print(select([User.c.PK, Info2.c.NAME]).select_from(
        join(User, Info2, User.c.PK==Info2.c.FK)))

print(select([User.c.PK, Info3.c.NAME]).select_from(
        join(User, Info3)))

engine.execute(select([User.c.PK, Info2.c.NAME]).select_from(
        join(User, Info2, User.c.PK==Info2.c.FK))).fetchall()

engine.execute(select([User.c.PK, Info3.c.NAME]).select_from(
        join(User, Info3))).fetchall()

conn = engine.connect()

conn.execute()

