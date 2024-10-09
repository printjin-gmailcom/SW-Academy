# https://nlp.stanford.edu/IR-book/newslides.html



trainingSet = [(1, 'Chinese Bejing Chinese', 'yes'), (2, 'Chinese Chinese Shanghai', 'yes'), (3, 'Chinese Macao', 'yes'), (4, 'Tokyo Japan C', 'no')]
testSet = [(5, 'Chinese Chinese Chinese Tokyo Japan')]



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'



from nltk.tokenize import word_tokenize
from nltk.text import Text

C = ('yes', 'no')

def training (C,D) :
    V = list()
    for d in D :
        for v in word_tokenize(d[1].lower()):
            if v not in V:
                V.append(v)

    N = len(D)

    prior = dict()
    condprob = dict()

    for c in C:

        Nc = len([d for d in D if d[-1] == c])

        prior[c] = Nc/N

        textc = Text(word_tokenize('\n'.join([d[1] for d in D if d[-1] == c]).lower()))

        for v in V:

            Tct = textc.count(v)

            for v in V:
                if v not in condprob:
                    condprob[v] = dict()

                condprob[v][c] = (textc.count(v)+1) / (textc.vocab().N()+len(V))
                # print(f'{textc.count(v)+1}+1/{len(V)}+{textc.vocab().N()}')

    return V, prior, condprob

training(C, trainingSet)

C = ('yes', 'no')

def training(C, D):
    V = list()
    for d in D:
        for v in word_tokenize(d[1].lower()):
            if v not in V:
                V.append(v)

    N = len(D)

    prior = dict()
    condprob = dict()
    for c in C:

        Nc = len([d for d in D if d[-1] == c])

        prior[c] = Nc/N

        textc = Text(word_tokenize('\n'.join([d[1] for d in D if d[-1] == c]).lower()))

        Tct = dict()
        for v in V:
            Tct[v] = textc.count(v)

        for v in V:
            if v not in condprob:
                condprob[v] = dict()

            condprob[v][c] = (textc.count(v)+1)/(textc.vocab().N()+len(V))

    return V, prior, condprob

V, prior, condprob = training(C, trainingSet)

from math import log

from math import log

def testing(C, V, prior, condprob, d):

    W = list()
    for t in d:
        W.append(word_tokenize(t[1].lower())) # 학습과 동일한 방식으로 토큰화

    score = list()
    for w in W:
        # 3
        score.append(dict())
        #print(f'P(c={c})={prior[c]}')

        for c in C:
            score[-1][c] = prior[c]
            for t in w:

                if t in V:
                    score[-1][c] += log(condprob[t][c])
                    #print(f'P({t}|{c})={condprob[t][c]}')

    return score, {(i+1):max(s, key=s.get) for i, s in enumerate(score)}

testing(C, V, prior, condprob, testSet)



# C, Dataset, Tokenizer, NB Classifier

from requests.sessions import Session

cookies = '''
BA_DEVICE	f33e7270-b2f6-4ffc-9ca4-b5f9c758327d
.blog.naver.com	/	2025-04-29T00:47:46.000Z	45					Medium
JSESSIONID	BDE33233C143B1ADBCFDB2A3F6B9429E.jvm1
m.blog.naver.com	/	Session	47	✓	✓			Medium
NIB2	BElAIHTY5ACxumZZr
.ni.naver.com	/	2025-05-05T02:42:37.740Z	21		✓	None		Medium
NID_AUT	IrP4IIhHxUkzQtE7fj+NGxgU6jW3HKcbFJfodPuHJjYtDvcsHA5seL/RCQ4/0EOA	.naver.com	/	Session	71	✓	✓	Lax		Medium
NID_JKL	a/ihRCNvhmCgH10WDzX09nwDRfP5xGY5iapyfxhQwjE=	.naver.com	/	Session	51		✓			Medium
NID_SES	AAABq2PpZUEtU71oLRD+V5ptkmapb7Ho0gk2Cdb9Sh0sHdyt8X40mLlEXRcfmIl8Cr36kzCE+oZxvBeozF/x1eFxBmK+itL23BNIpnBsOch+9Jo8t0fCXX/+7v1xHYVJpOWI3u5ECeIfIl/+l3qTZ3JaO8vZmW7QAkO6Tc1lRKYPB7+WewCusOkTamYs2F2TbGD30mRlxnon+aSZnkhy1L5gOWKZ6bEyIKhf2SK9LqkjLFsH3gmx8lOUxckQm0GSk1FPSzxoaJysW7atGqGorFGVtnfLRWYTsjZInFuwXW0sSRHLNeLCt5FcL9mR0qq6AoWC5kVB2GrISeprQRzTQveZo+5hBZyrNG5HDFXvOlm3F4mhcBktnwcj1EiFkzeF+sOfEcz0Phm0FmauWiV+EJ4viKrkePPmwIUUXWATWq1GNTSB78M9ScZz4NhKq3QHwy+CieGZ0T/vbN5TrJKpIBGZ/CQEiavhQVn8wsvw42iDj2BDGa+9/Q4HosMdnp3I/TEuNy91LFP+Ao7YJhH9j8frGgODtZ/cT1AnH3wNoXEt7mdeO6xbNdxYcfvJEJm/yQc/Bg==	.naver.com	/	Session	591		✓	Lax		Medium
NMUSER	YmbmFAEwaqbsKoKZFotd1z0N1HKqKAUsKxbwKxvqaAbrFqn9KxUmaqgsaqRJaqtXFxEqaAnDKqgs6xRpaZnlad/sxoRaad/sadUsaqROW9e7EoRpadUsawlGW430DVdq74lR74lC+4kZ74FTWLm/axgmaXF0Mre5pzJZDL9GW430DVdq74lR74lC+4kZ74FTWLm/axgmam==
mail.naver.com	/	Session	210					Medium
NM_srt_chzzk	1
www.naver.com	/	2024-04-01T02:42:02.000Z	13					Medium
NNB	SXVIUVDARX7GK	.naver.com	/	2025-05-06T02:33:21.999Z	16		✓	None		Medium
NWB	600a158aabe1cdfb133dce3c64f36c7a.1710202265888
.wcs.naver.com	/	2025-05-05T06:04:54.948Z	49		✓	None		Medium
isShownNewLnb	Y
news.naver.com	/	2025-04-19T01:46:28.960Z	14					Medium
ncvid	#vid#_211.234.204.168KNIJ
.cafe.naver.com	/	2025-05-05T02:42:24.893Z	30					Medium
nid_buk	PG7UHV46ULXWK
.nid.naver.com	/	2025-04-23T08:22:27.827Z	20		✓			Medium
nid_inf	581163939	.naver.com	/	Session	16					Medium
nid_slevel	1
.nid.naver.com	/	2025-04-01T02:32:44.000Z	11					Medi
'''

sess = Session()
for line in cookies.splitlines():
    if len(line) > 1:
        c = line.split()
        sess.cookies.set(c[0], c[1])

import re

url = 'https://mail.naver.com/json/list'

params = {
    "folderSN": 0,
    "page":1,
    "viewMode":'time',
    'previewMode' : 1,
    'sortField' : 1,
    'sortType' : 0,
    'u':'highs302'
}

dataset = list()
for i in range(1,10):
    params['page'] = i
    resp = sess.post(url, params=params)
    if re.search(r'text/plain', resp.headers['content-type']):
        for mail in resp.json()['mailData']:
            dataset.append((mail['subject'], 'ham'))

params['folderSN'] = 5

for i in range(1,10):
    params['page'] = i
    resp = sess.post(url, params=params)
    if re.search(r'text/plain', resp.headers['content-type']):
        for mail in resp.json()['mailData']:
            dataset.append((mail['subject'], 'ham'))

len(dataset)

dataset



# 스팸 분류기 성능 - data | feature | tokenizer | precision | recall

for i in range(len(dataset)):
    if dataset[i][0][0:4] == '(광고)':
        print('spam')
        print(dataset[i][0])
    else:
        print('N')



