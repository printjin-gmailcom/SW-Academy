import sqlite3

#                      SQL              -> data
# 1Python ------------> 2DBMS ------------> 3DB
#                     SQLite
# package sqlite3 func(SQL)
# 아무짓도 안함. data 이미 db 가정 -> 3
# python->select->sqlite db로 data 가져옴 -> 2 (cursor)
#         fetch(cursor -> obj) -> 1

# DBMS - Server, Sqlite serverless
# 1. connection => Client -> Server
# 2. cursor(작업)
# sqlite3.connect('파일경로', ':memory:')

# DBMS - Server, Sqlite serverless
# 1. connection => Client -> Server
# 2. cursor(작업)
# sqlite3.connect('파일경로', ':memory:')

# http://www.naver.com:80/index.html
# naver, 네이버
# dbms://id@host:port/databse
# ----   -- 파일경로---- ------

conn = sqlite3.connect('test.db')

type(conn)

cur = conn.cursor()

type(cur)

conn.close()

conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur

# cur.execute #한번
# cur.executemany #동일한 SQL, N번
# cur.executescript #여러 SQL

cur.execute('''
    CREATE TABLE CITY (
        PK INTEGER PRIMARY KEY,
        NAME VARCHAR(1)
    );
''')
# CITY, SUPPLIER, PART, SELLS

cur.execute('''
    INSERT INTO CITY (PK, NAME) VALUES (1, "안암점");
''')

# Qmark
gu = '성북구'
cur.execute('''
    INSERT INTO CITY (NAME) VALUES (?)
''', (gu,))

# Named
gu = '성북구'
cur.execute('''
    INSERT INTO CITY (NAME) VALUES (:key)
''', {'key':gu})

cur.executemany('''
    INSERT INTO CITY (NAME) VALUES (?);
''', (('노원구',), ('강북구',), ('중구',)))

# Python -> Obj을 dbms 전달하는 방법 (Q, Named)
# SQL(PK:primary key = 1)

cur.lastrowid

cur.execute('SELECT * FROM CITY')

city = cur.fetchall()

type(city), len(city)

# city[0] = fetchone
# city[:4] = fetchmany

conn.close()



conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur.execute('SELECT * FROM CITY')

cur.fetchall()

conn.commit()

cur.executescript('''
    DROP TABLE IF EXISTS SUPPLIER;
    CREATE TABLE SUPPLIER (
        PK INTEGER PRIMARY KEY,
        NAME TEXT,
        FK INTEGER NOT NULL
    );

    DROP TABLE IF EXISTS PART;
    CREATE TABLE PART (
        PK INTEGER PRIMARY KEY,
        NAME TEXT
    );

    DROP TABLE IF EXISTS SELLS;
    CREATE TABLE SELLS (
        FK1 INTEGER NOT NULL,
        FK2 INTEGER NOT NULL
    );
''')

# Qmark
cur.executemany('''
    INSERT INTO CITY (PK, NAME) VALUES(?, ?)
''', ((1, '성북구'), (2, '강북구'), (3, '중구')))

# Named
cur.executemany('''
    INSERT INTO PART VALUES(:no, :name)
''', ({'no':1,'name':'아메리카노'}, {'no':2,'name':'카페라떼'},
      {'no':3,'name':'바닐라라떼'}, {'no':4,'name':'아이스티'}))

conn.commit()

conn.close()



conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('SELECT * FROM CITY, PART')
cur.fetchall()

# SUPPLIER - 지점
# cur.execute('INSERT INTO SUPPLIER VALUES(1,"안암점",?)')
gu = '성북'
cur.execute('''
    SELECT PK
    FROM CITY
    WHERE NAME LIKE ?
    ORDER BY PK ASC
    LIMIT 0, 1
''', ('%'+gu+'%',))
rst = cur.fetchone()
fk = None if rst == None else rst[0]

store = '안암점'
if fk is not None:
    cur.execute('''
        INSERT INTO SUPPLIER VALUES(NULL, ?, ?);
    ''', (store, fk))

cur.execute('SELECT * FROM SUPPLIER')
cur.fetchall()

# 중첩 SQL
cur.execute('''
    INSERT INTO SUPPLIER VALUES(NULL, ?, (
        SELECT PK
        FROM CITY
        WHERE NAME LIKE ?
        ORDER BY PK ASC
        LIMIT 0, 1
    ));
''', ('종암점', '%성북%'));

cur.execute('SELECT * FROM SUPPLIER')
cur.fetchall()

cur.executemany('''
    INSERT INTO SUPPLIER VALUES(NULL, ?, (
        SELECT PK
        FROM CITY
        WHERE NAME LIKE ?
        ORDER BY PK ASC
        LIMIT 0, 1
    ));
''', (('3호점', '%강북%'), ('1호점', '%중%'), ('3호점', '%성북%'),
      ('2호점', '%강북%')));

cur.executemany('''
    INSERT INTO SELLS VALUES(?, ?)
''', ((1,1),(1,2),(2,1),(2,2),(3,4),(4,3),(5,2),(6,1),(7,1)))

conn.commit()

cur.execute('SELECT * FROM SELLS')
cur.fetchall()

# CITY - SUPPLIER(*); LEFT JOIN
cur.execute('''
    SELECT B.NAME, A.NAME FROM SUPPLIER AS A
    LEFT JOIN CITY AS B
    ON B.PK = A.FK
    ORDER BY B.NAME ASC
''')
cur.fetchall()

cur.execute('''
    SELECT B.NAME, COUNT(A.NAME) FROM SUPPLIER AS A
    LEFT JOIN CITY AS B
    ON B.PK = A.FK
    GROUP BY B.PK
    ORDER BY B.NAME ASC
''')
cur.fetchall()

# SUPPLIER - PART - SELLS
cur.execute('''
    SELECT B.NAME, C.NAME
    FROM SELLS AS A
    INNER JOIN SUPPLIER AS B
    ON B.PK = A.FK1
    INNER JOIN PART AS C
    ON C.PK = A.FK2
''')
cur.fetchall()

cur.execute('''
    SELECT A.NAME, COUNT(C.NAME)
    FROM PART AS A
    LEFT JOIN SELLS AS B
    ON A.PK = B.FK2
    INNER JOIN SUPPLIER AS C
    ON B.FK1 = C.PK
    GROUP BY A.PK
''')
cur.fetchall()

cur.execute('''
    SELECT A.NAME, C.NAME, COUNT(C.NAME)
    FROM SUPPLIER AS A
    LEFT JOIN SELLS AS B
    ON A.PK = B.FK2
    INNER JOIN PART AS C
    ON B.FK1 = C.PK
    GROUP BY C.PK
''')
cur.fetchall()

cur.execute('''
    SELECT D.NAME, A.NAME, C.NAME, COUNT(C.NAME)
    FROM SUPPLIER AS A
    LEFT JOIN SELLS AS B
    ON A.PK = B.FK2
    INNER JOIN PART AS C
    ON B.FK1 = C.PK
    INNER JOIN CITY AS D
    ON D.PK = A.FK
    GROUP BY C.PK
''')
cur.fetchall()

