# Tokenizing ; Feature Extraction

# splt, splitlines
# sent_tokenize
# word_tokenize, regex_tokenize, tweettokenize

# morheme analyze, POS tagger, Nouns Extractor -> tagset

# Ngram -> Tokenize(collocation), Language Model(P(t+1|t1...1))
#                                 -> 띄어쓰기, 다음 단어 예측

# Branch Entropy, Perplexity(Cohesion score) -> subword

# BPE -> WPM -> SPM


# [Normalization ; Feature Selection]
# Punk?  -> ',., -> format
# case, stopwords(most frequently...) -> Zipf
#       -> 한글? 'to be or not to be' -> X, Ngram(명사군+은,는,이,가...)
#       -> 메세지, 욕설 필터링

# [Edit Distance]
# 아녕하세요 -> 안녕+하세요
# Hamming, Levin -> dkssud (자동한글변경), 골려대 (오타수정)


# 다음주
# Naive Bayes, Regression (Linear, Logistic)(이항분포/다항분포, 연속확률분포 ), Gradient Methos (Asc, Desc)
# P(D|theta), Neural Network (ANN, Perception, SLP)
#             Layer(Weight), Output(Loss-J; Binary, Multinomial, Softmax, Activate Func.), MLP, DNN



import os
'JAVA_HOME' in os.environ
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-22'

from konlpy.tag import Hannanum, Kkma, Komoran, Okt

ma = list()
ma.append(Hannanum())
ma.append(Kkma())
ma.append(Komoran())
ma.append(Okt())

d = '''
통계청은 2024년 2월 산업활동동향을 통해 지난달 전(全)산업 생산지수(계절조정·농림어업 제외)는 115.3(2020년=100)으로 전월보다 1.3% 늘었다고 29일 밝혔다.

전산업 생산은 작년 11월 0.3% 증가로 반등한 이후 12월(0.4%)과 1월(0.4%), 2월(1.3%)까지 4달 연속 증가하고 있다. 부문별로 보면 광공업 생산이 3.1% 늘어 지난해 11월 이후 3개월 만에 증가 전환했다. 반도체와 기계 장비 등 제조업 생산이 3.4% 증가한 영향이다.
'''

from collections import Counter

dc = Counter([pos[1] for pos in ma[0].pos(d)])

dc

sum(Counter([pos[1] for pos in ma[0].pos(d)]).values())

Counter([pos[1] for pos in ma[0].pos(d) if pos[1] =='J'])

Counter([pos[1] for pos in ma[0].pos(d) if pos[1] =='E'])

Counter([pos[1] for pos in ma[0].pos(d) if pos[1] =='S'])

ma[0].tagset['X']

ma[0].tagset['M']

stopwords = ['J', 'E', 'X', 'M']
''.join([pos[0] for pos in ma[0].pos(d) if pos[1] not in stopwords])

len([pos[0] for pos in ma[0].pos(d) if pos[1] not in stopwords])

Counter([pos[0] for pos in ma[0].pos(d)]).values()

sum(Counter([pos[0] for pos in ma[0].pos(d)]).values())

ma[1].tagset

import re

len([pos[0] for pos in ma[1].pos(d) if re.match(r'N|V', pos[1])])

# 한글일떄, Zipf, 품사, 음절

[pos[0] for pos in ma[0].pos(d) if len(pos[0]) > 1]

len([pos[0] for pos in ma[0].pos(d) if len(pos[0]) > 1])

''.join([pos[0] for pos in ma[0].pos(d) if len(pos[0]) > 1])

len(([pos[0] for pos in ma[1].pos(d) if len(pos[0]) > 1]))

''.join([pos[0] for pos in ma[1].pos(d) if len(pos[0]) > 1])

len(([pos[0] for pos in ma[2].pos(d) if len(pos[0]) > 1]))

''.join([pos[0] for pos in ma[2].pos(d) if len(pos[0]) > 1])

len(([pos[0] for pos in ma[3].pos(d) if len(pos[0]) > 1]))

''.join([pos[0] for pos in ma[3].pos(d) if len(pos[0]) > 1])

len([pos[0] for pos in ma[1].pos(d) if len(pos[0]) > 1 and re.match(r'N|V', pos[1])])

''.join([pos[0] for pos in ma[1].pos(d) if len(pos[0]) > 1 and re.match(r'N|V', pos[1])])



#1. 사전베이스

stopwords = ['시발']

d = '시발'
''.join([t for t in d.split() if t not in stopwords])

r = list()
for t in d.split():
    if t in stopwords:
        r.append('*'*len(t))
    else:
        r.append(t)
''.join(r)

stopwords = ['시발', '씨발']

d = '시발 씨발'
''.join([t for t in d.split() if t not in stopwords])

r = list()
for t in d.split():
    if t in stopwords:
        r.append('*'*len(t))
    else:
        r.append(t)
' '.join(r)

# 2. 정규식

stopwords = re.compile('(시발|씨발|시방)')

d = '시발 씨발 시방 시발놈'

r = list()
for t in d.split():
    r.append(stopwords.sub('*'*len(stopwords.search(t).group(1)), t))
' '.join(r)

p = re.compile('선*물.*포.*장')

d = ['선물포장', '선물 포장', '선 물 포 장']

for t in d:
    if p.search(t):
        print(t)



# # https://happygrammer.github.io/nlp/sub-words-model/

# import re, collections

# def get_stats (vocab):
#     pairs = collections.defaultdict (int)
#     for word, freq in vocab.items():
#     symbols = word.split()
#     for i in range (len (symbols)-1):
#         pairs [symbols [i], symbols [i+1]] += freq
#     return pairs

# def merge_vocab (pair, v_in):
#     v_out = {}
#     bigram = re.escape(' '.join(pair))
#     p = re.compile(r' (?<!\S) ' + bigram + r' (?!\S)')
#     for word in v_in:
#         w_out = p.sub('.join (pair), word)
#         v_out [w_out] = v_in[word]
#     return v_out

# vocab =  {'l o w </w>' 5, 'l o w e r </w>': 2, 'n e w e s t </w>':6, 'w i d e s t </w>':3}
# num_merges = 10
# for i in range (num_merges) :
#     pairs = get_stats (vocab)
#     best = max (pairs, key-pairs.get)
#     vocab = merge_vocab (best, vocab)
#     print (best)

from nltk.tokenize import word_tokenize

data = ''' low low low low low
            lOwer Lower
            newest Newest newest newest newest newest
            widest widest widest'''

vocab = {}
for token in word_tokenize(data.lower()):
    token = ''.join(token)
    if token in vocab.keys():
        vocab[token] += 1
    else:
        vocab[token] = 1
vocab

data = ''' low low low low low
            lOwer Lower
            newest Newest newest newest newest newest
            widest widest widest'''

vocab = {}
for token in word_tokenize(data.lower()):
    token = ' '.join(token)
    if token in vocab.keys():
        vocab[token] += 1
    else:
        vocab[token] = 1
vocab

data = ''' low low low low low
            lOwer Lower
            newest Newest newest newest newest newest
            widest widest widest'''

vocab = {}
for token in word_tokenize(data.lower()):
    token = ' '.join(token) + '</w>'
    if token in vocab.keys():
        vocab[token] += 1
    else:
        vocab[token] = 1
vocab

data = ''' low low low low low
            lOwer Lower
            newest Newest newest newest newest newest
            widest widest widest'''

vocab = {}
for token in word_tokenize(data.lower()):
    token = ' '.join(token) + ' </w>'
    if token in vocab.keys():
        vocab[token] += 1
    else:
        vocab[token] = 1
vocab

def getPairs(v, n=2):
    pairs = dict()

    for k, v in v.items():
        tokens = k.split()
        for i in range(len(tokens)-(n-1)):
            token = ' '.join(tokens[i:i+n])

            if token not in pairs:
                pairs[token] = v
            else:
                pairs[token] += v

    return pairs

getPairs(vocab)

pairs = getPairs(vocab)
sorted(pairs, key=pairs.get)

sorted(pairs, key=pairs.get)[0]

pairs = getPairs(vocab)
sorted(pairs, key=pairs.get, reverse=True)

sorted(pairs, key=pairs.get, reverse=True)[0]

pairs.get('l o')

pairs = getPairs(vocab)
max(pairs, key=pairs.get)

best = max(pairs, key=pairs.get)

best

import re

def mergePairs(b, v):
    vocab = dict()

    for k, v in v.items():
        print(re.search(b, k))

mergePairs(best, pairs)

def mergePairs(b, v):
    vocab = dict()

    for k, v in v.items():
        newk = re.sub(k, ''.join(k), k)
        vocab[newk] = v

    return vocab

mergePairs(best, pairs)

def mergePairs(b, v):
    vocab = dict()

    for k, v in v.items():
        print(re.search(b, k), ''.join(k))
        newk = re.sub(b, ''.join(k), k)
        vocab[newk] = v

    return vocab

mergePairs(best, pairs)

def mergePairs(b, v):
    vocab = dict()

    for k, v in v.items():
        newk = re.sub(b, re.sub(' ','', k), k)
        vocab[newk] = v

    return vocab

mergePairs(best, pairs)

def mergePairs(b, v):
    vocab = dict()

    for k, v in v.items():
        newk = re.sub(b, re.sub(' ','', b), k)
        vocab[newk] = v

    return vocab

mergePairs(best, vocab)

data = ''' low low low low low
            lOwer Lower
            newest Newest newest newest newest newest
            widest widest widest'''

def getData(d):
    vocab = {}
    for token in word_tokenize(d.lower()):
        token = ' '.join(token) + ' </w>'
        if token in vocab.keys():
            vocab[token] += 1
        else:
            vocab[token] = 1

    return vocab

def getPairs(v, n=2):
    pairs = dict()

    for k, v in v.items():
        tokens = k.split()
        for i in range(len(tokens)-(n-1)):
            token = ' '.join(tokens[i:i+n])

            if token not in pairs:
                pairs[token] = v
            else:
                pairs[token] += v

    return pairs

getPairs(vocab)

def mergePairs(b, v):
    vocab = dict()

    for k, v in v.items():
        newk = re.sub(b, re.sub(' ','', b), k)
        vocab[newk] = v

    return vocab

vocab = getData(data)

for i in range(10):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    vocab = mergePairs(best, vocab)

vocab.keys()

[re.sub(r'</w>','',t).split() for t in vocab.keys()]

vocab = getData(data)

for i in range(6):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    vocab = mergePairs(best, vocab)

[re.sub(r'</w>','',t).split() for t in vocab.keys()]

[t.split() for t in vocab.keys()]

# low
# low e r
# ne w est
# w i d est

# low + ?
# ? + est

data = ' 시발 시발 시발 시발 시이발 씨발 씨발 씨발'

vocab = getData(data)

for i in range(1):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    vocab = mergePairs(best, vocab)
[re.sub(r'</w>',' ',t).split() for t in vocab.keys()]

data = ' 시발 시발 시발 시발 시이발 씨발 씨발 씨발'

vocab = getData(data)

for i in range(2):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    vocab = mergePairs(best, vocab)
[re.sub(r'</w>',' ',t).split() for t in vocab.keys()]

data = ' 시발 시발 시발 시발 시이발 씨발 씨발 씨발'

vocab = getData(data)

for i in range(3):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    vocab = mergePairs(best, vocab)
[re.sub(r'</w>',' ',t).split() for t in vocab.keys()]

data = ' 시발 시발 시발 시발 시이발 씨발 씨발 씨발'

vocab = getData(data)

for i in range(4):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    vocab = mergePairs(best, vocab)
[re.sub(r'</w>',' ',t).split() for t in vocab.keys()]

data = ' 시발 시발 시발 시발 시이발 씨발 씨발 씨발 시~발'

vocab = getData(data)
bestList = list()

for i in range(4):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    bestList.append(best)
    vocab = mergePairs(best, vocab)
[t.split() for t in vocab.keys()], bestList

def getData2(d):
    vocab = {}
    for token in word_tokenize(d.lower()):
        token = '<w> ' + ' '.join(token) + ' </w>'
        if token in vocab.keys():
            vocab[token] += 1
        else:
            vocab[token] = 1

    return vocab

data = '시발 시발 시발 시발 시이발 씨발 씨발 씨발 시~발'

vocab = getData2(data)
bestList = list()

for i in range(4):
    pairs = getPairs(vocab)
    best = max(pairs, key=pairs.get)
    bestList.append(best)
    vocab = mergePairs(best, vocab)
[t.split() for t in vocab.keys()], bestList

for p in bestList:
    print(re.sub(r'</?w>', r'\b', p))

start = list()
end = list()
stopwords = list()

for p in bestList:
    if re.match('<w>', p):
        start.append(re.sub('<w>', r'\b', p))
    if re.match('<\/w>', p):
        start.append(re.sub('<\/w>', r'\b', p))

start, end

start = list()
end = list()
stopwords = list()

for p in bestList:
    if re.match('<w>', p):
        start.append(re.sub('<w>', r'\\b', p))
    if re.search('<\/w>', p):
        start.append(re.sub('<\/w>', r'\\b', p))

start, end

start = list()
end = list()
stopwords = list()

for p in bestList:
    p = re.sub('\s', ' ', p)

    if re.match('<w>', p):
        start.append(re.sub('<w>', r'\\b', p))
    if re.search('<\/w>', p):
        start.append(re.sub('<\/w>', r'\\b', p))

patterns = list()
for s in start:
    for e in end:
        patterns.append(re.compile(s+'.*?'+e))
patterns

start = list()
end = list()
stopwords = list()

for p in bestList:
    if re.match('<w>', p):
        start.append(re.sub('<w>', r'\b', p))
    if re.search('<\/w>', p):
        end.append(re.sub('<\/w>', r'\b', p))

patterns = list()
for s in start:
    for e in end:
        patterns.append(re.compile(s+'.+?'+e))
patterns

start = list()
end = list()
stopwords = list()

for p in bestList:
    p = re.sub(r'\s', ' ', p)

    if re.match('<w>', p):
        start.append(re.sub('<w>', r'\b', p))
    if re.search('<\/w>', p):
        end.append(re.sub('<\/w>', r'\b', p))

patterns = list()
for s in start:
    for e in end:
        patterns.append(re.compile(s+'.+?'+e))
patterns

q = '시발'.split()

for t in q:
    for p in patterns:
        print(p)
        if p.search(t):
            print(t, '*'*len(t))

q = '시발 씨이발 시이발'.split()

for t in q:
    for p in patterns:
        if p.search(t):
            print(t, '*'*len(t))



# 음절 > 자음, 모음 > 초성, 중성, 종성

ord('가'), ord('힣'), ord('가')-ord('힣')

[chr(ord('가')+i) for i in range(28)]

[chr(ord('가')+(28*i)) for i in range(21)]

[chr(ord('가')+(28*21*i)) for i in range(19)]

28*21*19

def chr2tri(c):
    r = c

    if len(c) == 1 and re.search(r'[가-힣]', c):
        r = c

    return r

chr2tri('가')

def chr2tri(c):
    r = c

    if len(c) == 1 and re.search(r'[가-힣]', c):
        code = ord(c) - ord('가')
        cho, temp = divmod(code, (28*21))
        jung, jong = divmod(temp, 28)
        r = (cho, jung, jong)

    return r

chr2tri('나')

def chr2tri(c):
    r = c

    if len(c) == 1 and re.search(r'[가-힣]', c):
        code = ord(c) - ord('가')
        cho, temp = divmod(code, (28*21))
        jung, jong = divmod(temp, 28)
        r = (cho, jung, jong)

    return r

chr2tri('까')

print([chr(ord('ㄱ')+i) for i in range(30)])

print([chr(ord('ㅏ')+i) for i in range(21)])

choList = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungList = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongList = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ','ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def chr2tri(c):
    r = c

    if len(c) == 1 and re.search(r'[가-힣]', c):
        code = ord(c) - ord('가')
        cho, temp = divmod(code, (28*21))
        jung, jong = divmod(temp, 28)
        r = (choList[cho], jungList[jung], jongList[jong])

    return r

chr2tri('꺍')

choList = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungList = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongList = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ','ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def chr2tri(c):
    r = c

    if len(c) == 1 and re.search(r'[가-힣]', c):
        code = ord(c) - ord('가')
        cho, temp = divmod(code, (28*21))
        jung, jong = divmod(temp, 28)
        r = ''.join((choList[cho], jungList[jung], jongList[jong]))

    return r

''.join([chr2tri(c) for c in '고려koreaㄷㅐ학굙'])

def tri2chr(*c):
    r = ''.join(c)
    if len(c) == 3:
        c[0]
        c[1]
        c[2]

    return r

tri2chr('A', 'B', 'C', 'D')

def tri2chr(*c):
    r = ''.join(c)
    if len(c) == 3:
        c[0]
        c[1]
        c[2]

    return r

tri2chr('ㄱ', 'ㅏ', ' ')

def tri2chr(*c):
    r = ''.join(c)

    if len(c) == 3:
        umjeol = choList.index(c[0])*21*28
        umjeol += jungList.index(c[1])*28
        umjeol += jongList.index(c[2])
        r = chr(ord('가')+umjeol)

    return r

''.join([chr2tri(c) for c in '고려koreaㄷㅐ학굙']), ''.join([tri2chr(chr2tri(c)) for c in '고려koreaㄷㅐ학굙']), ''.join([tri2chr(*tuple(chr2tri(c))) for c in '고려koreaㄷㅐ학굙'])



def hamming(s1, s2):
    r = 0

    if len(s1) != len(s2):
        r = None
    else:
        r = sum([1 if c1 != c2 else 0 for c1, c2 in zip(s1, s2)])

    return r

hamming('안녕하세요', '아녕하세요')

hamming('안녕하세요', '아녕하세요') / len('안녕하세요')

c1 = ''.join([chr2tri(c) for c in '안녕하세요'])
c2 = ''.join([chr2tri(c) for c in '아녕하세요'])

hamming(c1, c2), hamming(c1, c2)/len(c1)



# Hamming
# 1. 다른 문자열 검사 x
# 2. 모든 문자를 동일하게 검사 (문자마다의 상대적 차이를 x)

# leven
# 삽입, 삭제 교체

# int LevenshteinDistance(char s[1..m], char t[1..m])
# {
#     declare int d[0..m, 0..n]
#     clear all emenets in d // set each element to zero

#     for i from 1 to m
#         d[i, 0] := i

#     for j from 1 to n
#         d[0, j] := j

#     for j from 1 to n
#     {
#         for i from 1 to m
#         {
#             if s[i] = t[j] then d[i, j] := d[i-1, j-1]
#             else d[i, j] := minimum(d[i-1, j]+1, d[i, j-1]+1, d[i-1, j-1]+1)
#         }
#     }
#     return d[m, n]
# }

# https://jino-dev-diary.tistory.com/entry/Algorithm-%EB%AC%B8%EC%9E%A5%EC%9D%98-%EC%9C%A0%EC%82%AC%EB%8F%84-%EB%B6%84%EC%84%9D-%ED%8E%B8%EC%A7%91-%EA%B1%B0%EB%A6%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Levenshtein-Distance

# lev(a, b) =
# |a| (if b = 0)
# |b| (if a = 0)
# lev(tail(a), tail(b)) (if a[0] = b[0])
# 1+ min (lev(tail(a), b), lev(a, tail(b)), lev(tail(a), tail(b))) (otherwise)

def lev(s1, s2):
    if len(s1) == 0:
        return len(s2)

    if len(s2) == 0:
        return len(s1)

    if s1[0] == s2[0]:
        return lev(s1[1:], s2[1:])

    else:
        l1 = lev(s1[1:], s2) + 1
        l2 = lev(s2, s1[1:]) + 1
        l3 = lev(s1[:1], s2[:1]) + 1
        return  min(l1, l2, l3)

lev('abc', 'abcde')

def lev(s1, s2):
    if len(s1) == 0:
        return len(s2)

    if len(s2) == 0:
        return len(s1)

    if s1[0] == s2[0]:
        return lev(s1[1:], s2[1:])

    else:
        l1 = lev(s1[1:], s2) + 1
        l2 = lev(s2, s1[1:]) + 2
        l3 = lev(s1[:1], s2[:1]) + 0.1
        return  min((l1, l2, l3))

lev('abccc', 'abcd')



