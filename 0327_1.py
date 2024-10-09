# Preprocessing ; 전처리
# Tokenizing -> Tokens = { 음절, 어절, 단어, 형태소, 어근, 접사, 어간, 어미, 구.. , ngram, 품사 ...}
#                      -> 왜? feature, 한정된 자원, 한정된 데이터, 한정된 모델 세상을 이해해야 함 (모델링)
# Zipf -> 빈도의 순으로 나열 = 순위의 역순이랑 동일
#      -> 고빈도 단어 (문장부호, 접사, 조사,..) : 상위 n개의 단어가 대부분 차지
#      -> 저빈도 단어 (고유명자, 신조어, 비속어, 오탈자, ..) : 토큰 후보들 중 대부분을 차지하는 너무 많음
# Heaps -> 문서에 나타난 고유의 단어들은 전체 단어의 수와 일정한 관계
#
# Tokenizing 기법
# NLTK -> sent_toeknize, word_tokenize -> regex_tokenize, TweetTokenize
# 한글 -> Morpheme Analyzer, POS, nouns, .., 품사표(tagset)
#      -> key를 못 찾음 ; Out Of Vocabulary (OOV) = [UNK]
# Entropy, Perplexity(Cohesion) -> 조건부확률 -> 어간
# Stemming (stem:어간) : 어간+어미
#                            -ed, ies, s, .. -> Porter
# Lemmatization (Lemma:표제어) : 어근/원형
#                               is was be .. -> be
#
# SPM - WPM - BPE (*)
# ; Senten-piece Model (문장;분절-띄어쓰기) -> 0
#       ; Word-piece Model (어절;분절) -> 중국어, 일본어
#             ; Bytes Pair Encoding (*)
#
# Normalizatioin
# 대소문자, 약어(D.C) , Stopwords



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'



from konlpy.tag import Hannanum

ma = Hannanum()

ma.nouns('인천 연수구 둥춘동에서 태어난 사람')

from konlpy.tag import Hannanum, Kkma, Komoran, Okt

ma = [Hannanum(), Kkma(), Komoran(), Okt()]

for m in ma:
    print(m.pos('하늘을 나는 새'))



! dir .\naver_news



# !rm -rf ./naver_news/

from os import mkdir

mkdir ('./news')

!dir

# from requests import get
# from requests.compat import urljoin
# from bs4 import BeautifulSoup
# import re

# urls = ['https://news.naver.com']
# seens = []
# path = './news/'

# while urls:
#     url = urls.pop(0)
#     resp = get(url)
#     seens.append(url)

#     if not re.search(r'text/html', resp.headers['Content-Type']):
#         continue

#     dom = BeautifulSoup(resp.text, 'html.parser')

#     # 1번 뉴스 메뉴
#     for a in dom.select('.Nlnb_menu_list > li > a[href]')[1:7]:
#         nurl = urljoin(url, a.attrs['href'])

#         if nurl not in urls and nurl not in seens:
#             urls.append(nurl)

#     # 2번 뉴스 헤드라인
#     for a in dom.select('id^="_SECTION_HEADLINE_LIST" .sa_text_title[href]'):
#         nurl = urljoin(url, a.attrs['href'])
#         if nurl not in urls and nurl not in seens:
#             urls.append(nurl)

#     # 3번 뉴스 본문
#     c = dom.select_one('#contents')
#     if c:
#         file_name = re.search(r'\/(\d{8,})$', url)
#         if file_name:
#             file_name = file_name.group(1)
#             with open(f'{path}{file_name}.txt', 'w', encoding='utf8') as f:
#                 f.write(c.text)

from requests import get
from requests.compat import urljoin
from bs4 import BeautifulSoup
import re

urls = ['https://news.naver.com']
seens = []
path = './news/'

while urls:
    url = urls.pop(0)
    resp = get(url)
    seens.append(url)

    if not re.search(r'text/html', resp.headers['Content-Type']):
        continue

    dom = BeautifulSoup(resp.text, 'html.parser')

    # 1번 뉴스 메뉴
    for a in dom.select('.Nlnb_menu_list > li > a[href]')[1:7]:
        nurl = urljoin(url, a.attrs['href'])

        if nurl not in urls and nurl not in seens:
            urls.append(nurl)

    # 2번 뉴스 헤드라인
    for a in dom.select('[id^="_SECTION_HEADLINE_LIST"] .sa_text_title[href]'):
        nurl = urljoin(url, a.attrs['href'])
        if nurl not in urls and nurl not in seens:
            urls.append(nurl)

    # 3번 뉴스 본문
    c = dom.select_one('#contents')
    if c:
        file = re.search(r'(\d{8,})$', url).group(1)
        with open(f'{path}{file}.txt', 'w', encoding='utf8') as f:
                f.write(c.text)

from os import listdir

def fileids(path):
    return list(map(lambda f:path + ('' if path[-1] == '/' else '/') +f, listdir(path)))

with open(fileids('news')[0], 'r', encoding='utf8') as f:
    d = f.read()



corpus = list()
for file in fileids('news'):
    with io.open(file, 'r', encoding='utf8') as f:
        corpus.append(
            re.sub(r'^\s+|\s+$', '',
               re.sub(r'\s+', ' ',
                    re.sub(r'\sCopyright.+$', ' ',
                      re.sub(r'[\xa0-\xff]', ' ', f.read())))))

len(corpus)

from nltk.text import Text
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt

PorterStemmer().stem('Play'), PorterStemmer().stem('Played'), PorterStemmer().stem('Playing'), PorterStemmer().stem('was')

t0bj = list()

for d in corpus:
    if len(t0bj) == 0:
        t0bj.append(Text(word_tokenize(d)).vocab())
    else:
        t0bj.append(t0bj[-1] + Text(word_tokenize(d)).vocab())

t0bj[-1].N(), t0bj[-1].B()

Kkmt0bj = list()

for d in corpus:
    if len(Kkmt0bj) == 0:
        Kkmt0bj.append(Text(ma[1].morphs(d)).vocab())
    else:
        Kkmt0bj.append(Kkmt0bj[-1] + Text(ma[1].morphs(d)).vocab())

Kkmt0bj[-1].N(), Kkmt0bj[-1].B()

n = 50
plt.plot([1/i for i in range(1, n+1)], c = 'k')
plt.plot([r[1]/t0bj[-1].get(t0bj[-1].max()) for r in t0bj[-1].most_common(n)], c = 'b')
plt.plot([r[1]/Kkmt0bj[-1].get(Kkmt0bj[-1].max()) for r in t0bj[-1].most_common(n)], c = 'r')

k = 12
b = .56
plt.plot([k.B() for k in Kkmt0bj], c='k')
plt.plot([12*k.N()**b for k in Kkmt0bj], c='r')

def ngram(s, n=2, t=True): # t=True;어절, False;음절
    result = []

    if not t:
        s = list(s)

    for i in range(len(s)-(n-1)):
        result.append(tuple(s[i:i+n]))

    return result

gram1 = list()
for c in corpus:
    gram1.extend(ngram(c, n=1, t=False))

gram2 = list()
for c in corpus:
    gram2.extend(ngram(c, n=1, t=False))

gram3 = list()
for c in corpus:
    gram3.extend(ngram(c, n=1, t=False))

gram4 = list()
for c in corpus:
    gram4.extend(ngram(c, n=1, t=False))

gram5 = list()
for c in corpus:
    gram5.extend(ngram(c, n=1, t=False))

gram1 = list()
gram2 = list()
gram3 = list()
gram4 = list()
gram5 = list()

for c in corpus:
    gram1.extend(ngram(c, n=1, t=False))
    gram2.extend(ngram(c, n=1, t=False))
    gram3.extend(ngram(c, n=1, t=False))
    gram4.extend(ngram(c, n=1, t=False))
    gram5.extend(ngram(c, n=1, t=False))

gram1, gram2, gram3, gram4, gram5

from collections import Counter

c1 = Counter(gram1)
c2 = Counter(gram2)
c3 = Counter(gram3)
c4 = Counter(gram4)
c5 = Counter(gram5)

n = 50
plt.plot([1/ i for i in range(1, n+1)], c= 'k')
plt.plot([i[1]/ max(c1.values()) for i in c1.most_common(n)], c= 'r')
plt.plot([i[1]/ max(c2.values()) for i in c2.most_common(n)], c= 'g')
plt.plot([i[1]/ max(c3.values()) for i in c3.most_common(n)], c= 'b')
plt.plot([i[1]/ max(c4.values()) for i in c4.most_common(n)], c= 'y')
plt.plot([i[1]/ max(c5.values()) for i in c5.most_common(n)], c= 'violet')

c3.most_common(50)

from nltk.tokenize import sent_tokenize

re.sub(r'\s', '', sent_tokenize(corpus[0])[0])

fileids('news')[0]

q = re.sub(r'\s', '', sent_tokenize(corpus[0])[0])

n = 1
for c in range(len(q)-(n-1)):
    k = tuple(q[c:c+n])
    print(k)
    base = c1.get(k, 0) # 없으면 오류 날 수 있음
    result = dict()
    for b in c2.keys():
        if b[:n] == k:
            result[b] = c2.get(b)/base
            print(b, c2.get(b)/base)
    print(sorted(result.items(), key=lambda r:r[1], reverse=True)[0])
    break

q = re.sub(r'\s', '', sent_tokenize(corpus[0])[0])

cdict = {1:c1, 2:c2, 3:c3, 4:c4, 5:c5}
n = 1

for c in range(len(q)-(n-1)):
    k = tuple(q[c:c+n])
    print(k)
    base = cdict[n].get(k, 0) # 없으면 오류 날 수 있음
    result = dict()
    for b in cdict[n+1].keys():
        if b[:n] == k:
            result[b] = cdict[n+1].get(b)/base
    print(sorted(result.items(), key=lambda r:r[1], reverse=True)[0])

q = re.sub(r'\s', '', sent_tokenize(corpus[0])[0])

cdict = {1:c1, 2:c2, 3:c3, 4:c4, 5:c5}
n = 1
s = list()
k = tuple(q[:n])
s.append(k)

for c in range(len(q)-(n-1)):
    k = k[-n:]
    base = cdict[n].get(k, 1) # 없으면 오류 날 수 있음
    result = dict()
    for b in cdict[n+1].keys():
        if b[:n] == k:
            result[b] = cdict[n+1].get(b)/base
    best = sorted(result.items(), key=lambda r:r[1], reverse=True)[0]
    if best[0][-1] == ' ':
        k += tuple(best[0][-1])
        s.append(tuple(' ',))
    k += tuple(q[c+n])
    s.append(k[-1:])

''.join([''.join(i) for i in s])

q

sent_tokenize(corpus[0])[0]

# Entropy(불확실정도) -> log

# Entropy(불확실정도) => log
# 8개의 공 => 공 1개가 무게가 다름
# log2 => 4 4 => 2 2 => 1 1 => 2^3 = 8 log2^3 => 3
# log3 => 3 3 3 => 1 1 1 => log2^3 = 2
# 50% 50% => p(A=true) = .5 =>
# |          *
# ---------1-----X
# |     *
# |  *
# |*
# |*      log
# |*

# |*
# |*
# |*
# | *
# |    *      -log=error= (실제정답 - 모델정답) <= error
# ---------1-----X
# |           *

# |
# |
# |
# |   *
# | *   *      P*-log
# -*-----*-1-----X
# |   + => 불확실성 높은 상태 => BCE(Binomial Cross Entropy)  => Loss(Error)

# - p * log p => 0 or 1
# Entropy=-P(A=true)*log(P(A=true))+-P(A=false)*log(P(A=false))
#        =-sigma(P(A=case)log(P(A=case)))

# 단어, 초고금리
#      초장
#      초
#      초??????
#      있다
#      있었다
#      있었고
#      있는데
#     [있]+?
#      초고+금
#      어근[L]+접사[R]
# Branch Entropy
# P(다음글자|처음부터 바로 이전글자)
#     ?   | A, B, C
# => P(A,B,C,?)     freq(A,B,C,?) => 4gram
#    ----------  =  -------------
#     P(A,B,C)        freq(A,B,C) => 3gram

def findKey(gram, key):
    k = tuple(key)
    return list(filter(lambda g:g[:len(k)] == k, gram.keys()))

findKey(c3, '가')

from math import log
key = '초'
base = c1.get(tuple(key))
be = 0.0

for k in findKey(c2, key):
    p = c2.get(k)/base
    be =+ -p*log(p)
    print('{} = {}/{} = {}'.format(k, c2.get(k), base, p))
print(key, be)

key = '가'
base = c2.get(tuple(key))
be = 0.0

for k in findKey(c3, key):
    p = c3.get(k)/base
    be =+ -p*log(p)
    print('{} = {}/{} = {}'.format(k, c3.get(k), base, p))
print(key, be)

key = '북'
base = c3.get(tuple(key))
be = 0.0

for k in findKey(c3, key):
    p = c4.get(k)/base
    be =+ -p*log(p)
    print('{} = {}/{} = {}'.format(k, c4.get(k), base, p))
print(key, be)

ma[1].morphs('창덕궁 달빛기행')



