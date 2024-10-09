# RDBMS(SQLite) -> Database
# Entity, Relation
# SQL --> DDL(CREATE, DROP), DML(INSERT, SELECT, UPDATE, DELETE)
# INSERT -> COLUMNS = VALUES 갯수 동일
# SELECT -> COLUMNS, WHERE;LIKE - % (아무거나), ==> REGULAR EXPRESSION
#          -> GROUP BY
#          -> ORDER BY
#          -> JOIN(CROSS, INNER, LEFT, RIGHT, OUTER)
# VIEW

import sqlite3

conn = sqlite3.connect('playlist.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE ARTIST(
        PK INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL DEFAULT '가수'
    );
''')

cur.executescript('''
    DROP TABLE IF EXISTS ALBUM;
    CREATE TABLE ALBUM(
        PK INTEGER PRIMARY KEY,
        NAME TEXT,
        FK INTEGER NOT NULL
    );

    CREATE TABLE GENRE(
        PK INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL
    );

    CREATE TABLE TRACK(
        PK INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        LENGTH INTEGER DEFAULT 0,
        RATING INTEGER DEFAULT 0,
        COUNT INTEGER DEFAULT 0,
        AFK INTEGER NOT NULL,
        GFK INTEGER NOT NULL
    );
''')

# DB Browser for SQLite 으로 시각화 가능

cur.executemany('''
    INSERT INTO ARTIST VALUES(NULL, ?);
''', [['수지'], ['박효신'], ['아이유']])

conn.commit()

cur.executemany('''
    INSERT INTO GENRE VALUES(NULL, ?);
''', [['발라드'], ['R&B'], ['락']])
conn.commit()

# artist -> PK
# INSERT album, FK=PK

def addAlbum(artist, album):
    cur.execute('SELECT PK FROM ARTIST WHERE NAME LIKE ?', ['%'+artist+'%'])
    PK = cur.fetchone()

    if PK:
        FK = PK[0]
        cur.execute('INSERT INTO ALBUM VALUES(NULL, ?, ?)', (album, FK))

    return PK, artist, album, cur.lastrowid

addAlbum('박효신', '박효신앨범') # 이걸로 추가

# album -> PK1, genre -> PK2
# INSERT track, AFK=PK1, GFK=PK2

def addTrack(album, genre, track, length=0, rating=0, count=0):
    cur.execute('SELECT PK FROM ALBUM WHERE NAME LIKE ?', ['%'+album+'%'])
    PK1 = cur.fetchone()

    cur.execute('SELECT PK FROM GENRE WHERE NAME LIKE ?', ['%'+genre+'%'])
    PK2 = cur.fetchone()

    if PK1 != None and PK2 != None:
        AFK = PK1[0]
        GFK = PK2[0]
        cur.execute('''
            INSERT INTO TRACK
            VALUES(NULL, :name, :length, :rating, :count, :afk, :gfk)
        ''', {'name':track, 'length':length, 'rating':rating, 'count':count,
              'afk':AFK, 'gfk':GFK})
        conn.commit()

    return PK1, PK2

addTrack('아이유', 'R&B', '아이유노래2') # 이거로 장르 추가, 안하면 None으로 뜸

cur.execute('''
    UPDATE TRACK
    SET NAME=?
    WHERE PK=?
''', ('박효신노래1', 4))

conn.commit() # 파일 변경하는 업데이트

cur.execute('SELECT * FROM TRACK')
cur.fetchall()

# 아티스트 - 앨범

cur.execute('SELECT DISTINCT(NAME) FROM ARTIST')
cur.fetchall()

cur.execute('SELECT * FROM ALBUM')
cur.fetchall()

cur.execute('''
    SELECT ARTIST.NAME, ALBUM.NAME
    FROM ARTIST
    LEFT JOIN ALBUM
    ON ALBUM.FK = ARTIST.PK
''')
cur.fetchall()

# (1)
# SELECT ______________
# FROM ARTIST

# (2)
# SELECT ______________
# FROM ARTIST
# INNER JOIN ALBUM
# ON ALBUM.FK = ARTIST.PK

# (3)
# SELECT ARTIST.NAME, ALBUM.NAME

cur.execute('''
    SELECT ARTIST.NAME, COUNT(ALBUM.NAME)
    FROM ARTIST
    INNER JOIN ALBUM
    ON ALBUM.FK = ARTIST.PK
    GROUP BY ARTIST.NAME
    ORDER BY ARTIST.NAME ASC
''')
cur.fetchall()

# ALBUM - TRACK(left)

cur.execute('''
    SELECT ALBUM.NAME, COUNT(TRACK.NAME)
    FROM ALBUM
    LEFT JOIN TRACK
    ON TRACK.AFK=ALBUM.PK
    GROUP BY ALBUM.PK
''')
cur.fetchall()

cur.execute('''
    SELECT ALBUM.NAME, COUNT(TRACK.NAME)
    FROM TRACK
    RIGHT JOIN ALBUM
    ON TRACK.AFK=ALBUM.PK
    GROUP BY ALBUM.PK
''')
cur.fetchall()

# GENRE - TRACK

cur.execute('''
    SELECT GENRE.NAME, COUNT(TRACK.NAME)
    FROM GENRE
    LEFT JOIN TRACK
    ON TRACK.GFK=GENRE.PK
    GROUP BY GENRE.PK
''')
cur.fetchall()

# ARTIST - ALBUM - TRACK

cur.execute('''
    SELECT A.NAME, B.NAME, C.NAME
    FROM ARTIST AS A
    LEFT JOIN ALBUM AS B
    ON B.FK = A.PK
    LEFT JOIN TRACK AS C
    ON C.AFK = B.PK
''')
cur.fetchall()

cur.execute('''
    SELECT A.NAME, B.NAME, B.TNAME
    FROM ARTIST AS A
    LEFT JOIN (
        SELECT ALBUM.FK, ALBUM.NAME AS NAME, TRACK.NAME AS TNAME
        FROM ALBUM
        LEFT JOIN TRACK
        ON TRACK.AFK = ALBUM.PK
    ) AS B
    ON B.FK = A.PK
''')
cur.fetchall()

cur.execute('''
    SELECT A.NAME, B.NAME, COUNT(C.NAME)
    FROM ARTIST AS A, ALBUM AS B, TRACK AS C
    WHERE A.PK=B.FK AND B.PK=C.AFK
    GROUP BY B.NAME
''')
cur.fetchall()

# 가수 - 앨범 - 장르 - 노래

cur.execute('''
    SELECT A.NAME, B.NAME, C.NAME, D.NAME
    FROM ARTIST AS A, ALBUM AS B, GENRE AS C, TRACK AS D
    WHERE A.PK=B.FK AND B.PK=D.AFK AND C.PK=D.GFK
''')
cur.fetchall()

cur.execute('''
    SELECT A.NAME, B.NAME, C.NAME, COUNT(D.NAME)
    FROM ARTIST AS A, ALBUM AS B, GENRE AS C, TRACK AS D
    WHERE A.PK=B.FK AND B.PK=D.AFK AND C.PK=D.GFK
    GROUP BY A.PK, B.PK, C.PK
''')
cur.fetchall()

cur.execute('''
    CREATE VIEW ALBUM_TRACK AS
    SELECT ALBUM.FK, ALBUM.NAME AS NAME, TRACK.NAME AS TNAME
        FROM ALBUM
        LEFT JOIN TRACK
        ON TRACK.AFK = ALBUM.PK
''')

cur.execute('SELECT * FROM ALBUM_TRACK')
cur.fetchall()

cur.execute('''
    SELECT A.NAME, B.NAME, B.TNAME
    FROM ARTIST AS A
    LEFT JOIN ALBUM_TRACK AS B
    ON B.FK = A.PK
''')
cur.fetchall()

conn.close()

# A JOIN B
# A  (LEFT )JOIN
#    (RIGHT )JOIN B



# SNS - 게시글/해시태그 등록/수정/삭제

conn = sqlite3.connect('sns.db')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE POST(
        PK INTEGER PRIMARY KEY
    );

    CREATE TABLE HASHTAG(
        PK INTEGER PRIMARY KEY,
        TAG TEXT NOT NULL,
        COUNT INTEGER DEFAULT 0
    );

    CREATE TABLE POSTTAG(
        PFK INTEGER NOT NULL,
        TFK INTEGER NOT NULL
    )
''')

cur.execute('''
    ALTER TABLE POST
    ADD COLUMN CONTENT TEXT
''')

conn.close()



conn = sqlite3.connect('playlist.db')
cur = conn.cursor()

cur.execute('''
    ALTER TABLE ARTIST
    ADD COLUMN temp TEXT NOT NULL DEFAULT ''
''')

conn.close()



conn = sqlite3.connect('sns.db')
cur = conn.cursor()

cur.execute('DELETE FROM POST')
cur.execute('DELETE FROM HASHTAG')
cur.execute('DELETE FROM POSTTAG')
conn.commit()

# POST 등록
def newPosting(content, *tags):
    # 1
    cur.execute('INSERT INTO POST VALUES(NULL, ?)', (content,))
    conn.commit()

    cur.execute('SELECT PK FROM POST ORDER BY PK DESC LIMIT 0, 1')
    fk = cur.fetchone()[0]

    # 2
    fkList = list()
    for tag in tags:
        cur.execute('SELECT PK FROM HASHTAG WHERE TAG=?', (tag,))
        if cur.fetchone() is None:
            cur.execute('INSERT INTO HASHTAG (TAG) VALUES (?)', (tag,))
            conn.commit()
        cur.execute('SELECT PK FROM HASHTAG WHERE TAG=?', (tag,))
        PK = cur.fetchone()[0]
        fkList.append(PK)
        cur.execute('UPDATE HASHTAG SET COUNT = COUNT + 1 WHERE PK=?', (PK,))
        conn.commit()

    # 3
    for FK in fkList:
        cur.execute('INSERT INTO POSTTAG VALUES(?,?)', (fk, FK))
    conn.commit()

    return fk, fkList

newPosting('내용1', 'python', 'orm')

def modifyPost(content, *tags):
    # 1. 게시글 찾는과정 - 내용이 항상 일치한다 가정
    cur.execute('SELECT PK FROM POST WHERE CONTENT=?', (content,))
    PPK = cur.fetchone()[0]

    # 2. 게시글에 달린 해시태그 목록
    cur.execute('SELECT TFK FROM POSTTAG WHERE PFK=?', (PPK,))
    tagList = list()
    for row in cur.fetchall():# [[1,],[]]
        tagList.append(row[0])

    # 3. 해시태그 찾는과정
    tpkList = list()
    for tag in tags:
        cur.execute('SELECT PK FROM HASHTAG WHERE TAG=?', (tag,))
        if cur.fetchone() is None:
            cur.execute('INSERT INTO HASHTAG (TAG) VALUES (?)', (tag,))
            conn.commit()

        cur.execute('SELECT PK FROM HASHTAG WHERE TAG=?', (tag,))
        TPK = cur.fetchone()[0]
        tpkList.append(TPK)

        # 기존 등록된 태그와 일치하지 않을시 추가
        if TPK not in tagList:
            cur.execute('UPDATE HASHTAG SET COUNT = COUNT + 1 WHERE PK=?', (TPK,))
            cur.execute('INSERT INTO POSTTAG VALUES(?,?)', (PPK, TPK))
            conn.commit()

    # 4. 삭제된 해시태그 찾는과정
    for tag in tagList:
        if tag not in tpkList:
            cur.execute('UPDATE HASHTAG SET COUNT = COUNT - 1 WHERE PK=?', (tag,))
            cur.execute('DELETE FROM POSTTAG WHERE PFK=? AND TFK=?', (PPK, tag))
            conn.commit()

modifyPost('내용1', 'python', 'alchemy')

