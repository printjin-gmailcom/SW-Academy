# https://www.cs.virginia.edu/~hw5x/Course/IR2021-Spring/docs/



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'

from konlpy.corpus import kobill
from konlpy.tag import Komoran
from nltk.tokenize import word_tokenize, sent_tokenize
import re

kobill.fileids()

def ngram(s, n=2):
    rst = list()
    for i in range(len(s)-(n-1)):
        rst.append(s[i:i+n])
    return rst

ma = Komoran()

V = list()

for f in kobill.fileids():
    d = kobill.open(f).read()
    d = re.sub(r'^\s|\s$', '', re.sub(r'\s+', '', d))
    V.extend(word_tokenize(d))
    V.extend(ngram(d, 2))
    V.extend(ngram(d, 3))
    V.extend(ma.morphs(d))
    V.extend(['/'.join(t) for t in ma.pos(d)])

len(V), len(set(V))

from collections import Counter

cv = Counter(V)

CV = list(set(V))

D = kobill.fileids()

DTM = [[0 for j in range(len(CV))] for i in range(len(D))]

len(DTM), len(DTM[0])

for f in D:
    i = D.index(f)

    d = kobill.open(f).read()
    d = re.sub(r'^\s|\s$', '', re.sub(r'\s+', '', d))

    for t in word_tokenize(d):
        j = CV.index(t)
        DTM[i][j] = 1

    V.extend(word_tokenize(d))
    V.extend(ngram(d, 2))
    V.extend(ngram(d, 3))
    V.extend(ma.morphs(d))
    V.extend(['/'.join(t) for t in ma.pos(d)])

for f in D:
    i = D.index(f)

    d = kobill.open(f).read()
    d = re.sub(r'^\s|\s$', '', re.sub(r'\s+', '', d))

    for t in word_tokenize(d) + ngram(d, 2) + ngram(d, 3) + ma.morphs(d) + ['/'.join(t) for t in ma.pos(d)]:
        j = CV.index(t)
        DTM[i][j] = 1

CV[:10]

'대통령' in CV

'국회' in CV

Q = '대통령 국민 국회'

rst = list()

for q in Q.split():
    k = CV.index(q)
    rst.append(list())
    for i, d in enumerate(DTM):
        for j, t in enumerate(d):
            if k == j and t == 1:
                rst[-1].append(i)

rst

candi = set(rst[0])

for r in rst[1:]:
    candi = candi.intersection(set(r))

list(candi)

rst

TDM = [[0 for j in range(len(D))] for i in range(len(CV))]

len(TDM), len(TDM[0])

for f in D:
    i = D.index(f)

    d = kobill.open(f).read()
    d = re.sub(r'^\s|\s$', '', re.sub(r'\s+', '', d))

    for t in word_tokenize(d) + ngram(d, 2) + ngram(d, 3) + ma.morphs(d) + ['/'.join(t) for t in ma.pos(d)]:
        j = CV.index(t)
        TDM[j][i] = 1

Q = '대통령 국민 국회'

rst = list()

for q in Q.split():
    k = CV.index(q)
    rst.append([i for i, v in enumerate(TDM[k]) if v == 1])

rst

# Array =! Linked List

# rst = [data|p] -> [data|p] -> [data|p]

# [d1, d2, d3 ...., d10]
# [d1 -> d3] -> [(i|다음주소), (i|다음주소), (i|다음주소)]

Dictionary = dict()
Posting = list()

for f in D:
    i = D.index(f)

    d = kobill.open(f).read()
    d = re.sub(r'^\s|\s$', '', re.sub(r'\s+', '', d))

    for t in word_tokenize(d) + ngram(d, 2) + ngram(d, 3) + ma.morphs(d) + ['/'.join(t) for t in ma.pos(d)]:
        j = CV.index(t)

        if t not in Dictionary:
            Dictionary[t] = len(Posting)
            Posting.append((i, -1))
        else:
            pos = Dictionary[t]
            Dictionary[t] = len(Posting)
            Posting.append((i, pos))

Dictionary['국민']

pos = Dictionary['국민']

while pos != -1:
    i, pos = Posting[pos]
    rst.append(i)

rst

pos = Dictionary['국민']

while pos != -1:
    i, pos = Posting[pos]
    rst.append((i, pos))

rst

rst = list()

pos = Dictionary['대통령']

while pos != -1:
    i, pos = Posting[pos]
    rst.append(i)

rst

list(set(rst))

from struct import pack, unpack

pack('i', 1)

pack('i', -1)

Dictionary = dict()

fp = open('posting.dat', 'wb')

for f in D:
    i = D.index(f)

    d = kobill.open(f).read()
    d = re.sub(r'^\s|\s$', '', re.sub(r'\s+', '', d))

    local = Counter(word_tokenize(d) + ngram(d, 2) + ngram(d, 3) + ma.morphs(d) + ['/'.join(t) for t in ma.pos(d)])

    for k, v in local.items():
        if k not in Dictionary:
            Dictionary[k] = fp.tell()
            fp.write(pack('iii', i, v, -1))
        else:
            pos = Dictionary[k]
            Dictionary[k] = fp.tell()
            fp.write(pack('iii', i, v, pos))
fp.close()

!dir \w *.dat

pos = Dictionary['국민']

fp = open('posting.dat', 'rb')
while pos != -1:
    fp.seek(pos)
    i, freq, npos = unpack('iii', fp.read(12))
    pos = npos
    print(i, freq)
fp.close()

from os import listdir

def fileids(path):
    return [path + ('/' if path[-1] != '/' else '') + f for f in listdir(path) if re.search(r'[.]txt$', f)]

len(fileids('./news'))

Collection = fileids('./news')

def preprocessing(d):
    d = re.sub(r'\s+', ' ', d)
    d = re.sub(r'^\s|s$', '', d)
    return d

with open(Collection[0], 'r', encoding='utf8') as fp:
    print(preprocessing(fp.read()))

Dictionary = dict()

pfp = open('Posting.dat', 'wb')

for f in Collection:
    with open(f, 'r', encoding='utf8') as fp:
        text = preprocessing(fp.read())

    localMap = dict()
    for t in word_tokenize(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    for t in ma.morphs(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    for t in ngram(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    i = Collection.index(f)
    for k, v in localMap.items():
        if k not in Dictionary:
            Dictionary[k] = pfp.tell()
            info = (i, v, -1)
            pfp.write(pack('iii', *info))
        else:
            info = (i, v, Dictionary[k])
            pfp.write(pack('iii', *info))
            Dictionary[k] = pfp.tell()

pfp.close()

Collection[0]

!dir \w *.dat



