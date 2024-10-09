# Vector Space Model -> Concept(BoW-Tokens)
# Importance? -> Weight = Zipf - TF(문서내 중요도)-IDF(문서간 중요도)
# Document, Query => Representation(Vector)
# Relevance-Simililarity? Distance vs. Angle
# 1. Distance => sum(tㅌV) => Extra tokens
# 2. Angle => tㅌQ and D, inner product => x1*x2+..., Overlapped(Projection)
#    => |Q| constant, |D| weight



from math import log

tf1 = lambda f: 1 if f > 0 else 0
tf2 = lambda f: f
tf3 = lambda f, s : f/s
tf4 = lambda f : log(f+1)
tf5 = lambda f, m : .5 + .5*(f/m)
tf6 = lambda k, f, m : k + (1-k)*(f/m)

idf1 = lambda df : 1
idf2 = lambda df, n: log(n/df)
idf3 = lambda df, n :log(n/(1+df)) + 1
idf4 = lambda df, m : log(m/(1+df))
idf5 = lambda df, n : log((n-df)/df)



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'

from konlpy.corpus import kobill
from konlpy.tag import Komoran
from nltk.tokenize import word_tokenize, sent_tokenize
from struct import pack, unpack
import re

ma = Komoran()

def ngram(s, n=2):
    rst = list()
    for i in range(len(s)-(n-1)):
        rst.append(s[i:i+n])
    return rst

from os import listdir

def fileids(path):
    return [path + ('/' if path[-1] != '/' else '') + f for f in listdir(path) if re.search(r'[.]txt$', f)]

len(fileids('./news'))

def preprocessing(d):
    d = d.lower()
    d = re.sub(r'[a-z0-9\-_.]{3,}@[a-z0-9\-_.]{3,}(?:[.]?[a-z]{2})+', ' ', d)
    d = re.sub(r'[‘’ⓒ\'\"“”…=□*◆:]', ' ', d)
    d = re.sub(r'\s+', ' ', d)
    d = re.sub(r'^\s|\s$', '', d)
    return d

def indexer(f): # Map
    with open(f, 'r', encoding='utf8') as fp:
        text = preprocessing(fp.read())

    localMap = dict()
    for t in word_tokenize(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    for s in sent_tokenize(text): # 메모리 오류
        for t in ma.morphs(s):
            if t not in localMap:
                localMap[t] = 0
            localMap[t] += 1

    for t in ngram(text):
        if t not in localMap:
            localMap[t] = 0
        localMap[t] += 1

    return localMap

def indexing(path):
    C = [{'no':i+1,'name':f,'maxfreq':0,'length':0.0} for i,f in enumerate(fileids(path))]
    Dictionary = dict()
    Posting = 'posting.dat'

    fp = open(Posting, 'wb')

    for i, f in enumerate(C):
        mapped = indexer(f['name'])
        for t, f in mapped.items():
            if f > C[i]['maxfreq']:
                C[i]['maxfreq'] = f

            if t not in Dictionary.keys():
                Dictionary[t] = dict()
                Dictionary[t]['ppos'] = fp.tell()
                Dictionary[t]['wpos'] = -1
                Dictionary[t]['df'] = 1
                fp.write(pack('iii', i, f, -1))
            else:
                Dictionary[t]['df'] += 1
                pos = Dictionary[t]['ppos']
                Dictionary[t]['ppos'] = fp.tell()
                fp.write(pack('iii', i, f, pos))

    fp.close()

    return C, Dictionary, Posting

C, V, posting = indexing('./news/')

N = len(C)

fp2 = open('weight.dat', 'wb')

with open(posting, 'rb') as fp:
    for t, info in V.items():
        df = info['df']
        V[t]['wpos'] = fp2.tell()
        pos = info['ppos']
        while pos != -1:
            fp.seek(pos)
            i, f, pos = unpack('iii', fp.read(12))
            w = tf6(0, f, C[i]['maxfreq']) * idf2(df, N)
            C[i]['length'] += w**2
            fp2.write(pack('if', i, w))
fp2.close()

data = '''
[서울=뉴시스]김래현 기자 = 목요일인 25일은 고기압 영향권에 들며 기온이 점차 올라 경상권 등에서 초여름 날씨가 나타나겠고 동쪽 지역을 중심으로는 황사 영향으로 미세먼지 농도가 높겠다.

기상청은 이날 "낮 최고기온이 경상권 등에서 25도 이상으로 올라 덥겠고 일교차가 15도 이상으로 크겠다"고 예보했다.

낮 최고기온은 18~27도를 오르내리겠다.

주요 지역 낮 최고기온은 서울 27도, 인천 24도, 수원 26도, 춘천 27도, 강릉 24도, 청주 28도, 대전 28도, 전주 29도, 광주 29도, 대구 29도, 부산 25도, 제주 25도다.

아침까지 바다 안개가 유입되는 중부서해안, 전북서해안과 경기남부내륙, 강원남부내륙, 충청권내륙, 전라권내륙, 경북권내륙을 중심으로 가시거리 200m 미만 짙은 안개가 끼는 곳이 있겠다.

당분간 서해상과 남해상, 제주도해상에는 바다 안개가 끼는 곳이 있겠고 강원동해안과 경상권해안에는 너울에 의한 높은 물결이 갯바위나 방파제, 해안도로를 넘을 수 있겠다.

내몽골 고원과 고비 사막에서 발원하고 있는 황사가 이날부터 동쪽지역을 중심으로 영향을 줄 가능성이 있겠다.

미세먼지는 전국이 '좋음'에서 '보통'으로 예상되지만 강원영동과 경북은 낮에 일시적으로 '나쁨' 수준으로 치솟겠다．
'''


qkv = indexer(fileids('./news/')[10])
qw = dict()
maxfreq = max(qkv.values())
ql = 0.0
N = len(C)
for t, f in qkv.items():
    if t in V:
        w = tf6(0, f, maxfreq)*idf2(V[t]['df'], N)
        qw[t] = w
        ql += w**2

result = dict()

with open('weight.dat', 'rb') as fp:
    for t, w in qw.items():
        if t not in V:
            continue

        info = V[t]
        i = 0
        while i < info['df']:
            fp.seek(info['wpos']+8*i)
            no, dw = unpack('if', fp.read(8))

            if no not in result:
                result[no] = 0.0

            result[no] += w*dw
            i += 1



from math import sqrt

result = {i:cos/(sqrt(ql)*sqrt(C[i]['length'])) for i, cos in result.items()}

K = 10
sorted(result.items(), key=lambda r:r[1], reverse=True)[:K]

C[13]['name']

with open(C[13]['name'], 'r', encoding='utf8') as f:
    print(f.read().strip())

with open(C[23]['name'], 'r', encoding='utf8') as f:
    print(f.read().strip())



from requests import get
from requests.compat import urljoin
from bs4 import BeautifulSoup
import re

url = 'https://news.naver.com'
path = './news/'

resp = get(url)
dom = BeautifulSoup(resp.text, 'html.parser')

for a in dom.select('.Nlnb_menu_list > li > a[href]')[1:7]:
    nurl = urljoin(url, a.attrs['href'])
    section = re.search(r'(\d{3})$', nurl).group(1)

    resp = get(nurl)
    dom = BeautifulSoup(resp.text, 'html.parser')
    for a in dom.select('[id^="_SECTION_HEADLINE_LIST"] .sa_text_title[href]'):
        resp = get(urljoin(url, a.attrs['href']))
        dom = BeautifulSoup(resp.text, 'html.parser')

        c = dom.select_one('#contents')
        if c:
            file = re.search(r'(\d{8,})$', resp.request.url).group(1)
            with open(f'{path}{section}-{file}.txt', 'w', encoding='utf8') as f:
                f.write(c.get_text())

from requests import get
from requests.compat import urljoin
from bs4 import BeautifulSoup
import re

urls = [('https://news.naver.com', 0)]
seens = []
path = './news/'

while urls:
    url = urls.pop(0)

    resp = get(url[0])
    seens.append(url[0])

    if not re.search(r'text\/html', resp.headers['content-type']):
        continue

    dom = BeautifulSoup(resp.text, 'html.parser')

    for a in dom.select('.Nlnb_menu_list > li > a[href]')[1:7]:
        nurl = urljoin(url[0], a.attrs['href'])
        if nurl not in urls and nurl not in seens:
            urls.append((nurl, seens.index(url[0])))

    for a in dom.select('[id^="_SECTION_HEADLINE_LIST"] .sa_text_title[href]'):
        nurl = urljoin(url[0], a.attrs['href'])
        if nurl not in urls and nurl not in seens:
            urls.append((nurl, seens.index(url[0])))

    c = dom.select_one('#contents')
    if c:
        section = re.search(r'(\d{3})$', seens[url[1]]).group(1)
        file = re.search(r'(\d{8,})$', url[0]).group(1)
        with open(f'{path}{section}-{file}.txt', 'w', encoding='utf8') as f:
            f.write(c.get_text())

from os import listdir

def fileids(path):
    return [path+('/' if path[-1] != '/' else '')+f for f in listdir(path) if re.search(r'\d+[-]\d+[.]txt$', f)]



K = 7
knn = dict()
for i, sim in sorted(result.items(), key=lambda r:r[1], reverse=True)[:K]:
    category = re.search(r'\/(\d{3})[-]', C[i]['name']).group(1)
    if category not in knn:
        knn[category] = 0.0

    knn[category] += sim

{k:v/sum(knn.values()) for k, v in knn.items()}



