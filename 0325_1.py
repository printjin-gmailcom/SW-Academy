# http://konlpy.org/ko/latest/
# JDK 1.8 이상 JPype1 0.5.7 이상

# https://konlpy.org/ko/latest/install/#id2
# https://code-algo.tistory.com/28

# -----내일까지 다운로드 받아두기-----

!pip install nltk

import nltk

nltk.download()

nltk.download('gutenberg')
nltk.download('punkt')

from nltk.corpus import gutenberg

gutenberg.fileids()

gutenberg.fileids()[0]

corpus = gutenberg.open(gutenberg.fileids()[0]).read()

corpus

from nltk.tokenize import sent_tokenize, word_tokenize, regexp_tokenize, TweetTokenizer

# 문서 = { 문단 .. } = {{ 문장 ... }}
# 문장이 문서를 구성하는 가장 작은 단위
# 문장을 분리해내야함

len(corpus.splitlines()), len(sent_tokenize(corpus))

sum([len(s) for s in sent_tokenize(corpus)])

sum([len(s) for s in sent_tokenize(corpus)])/7493

sent_tokenize('한글에서는 어떻게 분리하는지 봅시다. 볼까요?')

sent_tokenize('한글에서는 어떻게 분리하는지 봅시다... 볼까요? 볼래요! ')

# v.?! 문장을 구분

data = '''
오는 2025학년도 대학 입시에서 의과대학 입학정원이 2000명이나 대폭 증원이 확정됐다. 지역 의료계 살리기에 나섰던 전국 지방자치단체들의 후속대책도 곧 마련될 것으로 보인다. 하지만 각 지자체의 의과대 유치전략들은 큰 온도차를 보이고 있다.

6일 각 지자체에 따르면 전남도와 경북도·포항시처럼 의대 유치에 적극 나서는 곳도 있지만, 전북이나 강원처럼 신규 의과대 유치에 미지근한 지자체 등으로 나뉘고 있다.

전국 시도 중 유일하게 의과대학이 없는 전남도는 '전남형 국립의대' 신설 필요성을 거듭 강조하고 100명 이상의 정원 배정을 강력히 요청하고 있다. 전남 지역은 연간 70만명이 치료를 받기 위해 타 지역에서 1조5000억원을 소비한다는 통계도 있다.
'''

len([s for s in data.splitlines() if len(s) > 1]), len(sent_tokenize(data))

len(corpus.split()), len(word_tokenize(corpus))

len(set(corpus.split())), len(set(word_tokenize(corpus)))

len(data.split()), len(word_tokenize(data)), len(set(data.split())), len(set(word_tokenize(data)))

set(word_tokenize(data))

len(regexp_tokenize(corpus, r'\b\w+\b')), len(set(regexp_tokenize(corpus, r'\b\w+\b')))

# word_tokenize, regexp_tokenize, TweetTokenizer
# 음절, 어절, 형태소 ...
# Ngram -> P, Markov Assumption
# entropy, perplexity -> p
# BPE, BT, SPT + MA
# tokenizing -> normaliing -> feature selection -> model

tt = TweetTokenizer()

tt.tokenize(':) =() ㅠㅠ'), word_tokenize(':) =() ㅠㅠ')

len(tt.tokenize(':) =() ㅠㅠ')), len(word_tokenize(':) =() ㅠㅠ'))

len(tt.tokenize(corpus)), len(word_tokenize(corpus))

# token -> 어절, 음절, 단어, 형태소, 어간, 어미, 어근, 접사, 구, 품사 ,,,

from nltk.text import Text

t = Text(word_tokenize(corpus))

# from collections import Counter

t.count('Emma')

t.vocab().B(), t.vocab().N(), len(t.tokens)

t.vocab().freq('Emma') #FreqDist

t.vocab().most_common(50)

t.collocations

t.count('Weston')

t.concordance('Emma')

t.dispersion_plot(['Emma', 'Weston', 'Elton'])

t.similar('Emma')

from nltk.collocations import BigramAssocMeasures

# BigramAssocMeasures().

# collocation(연어), co-occurence(공기어)
# -> 이웃한 패턴      -> 같이 자주 나오는 표현

from nltk.collocations import BigramCollocationFinder

bigram = BigramCollocationFinder.from_words(word_tokenize(corpus))

bigram.nbest(BigramAssocMeasures.pmi, 10)

# Ngram -> Language Model

print(data)

# P(의과대학|정부의)
# P(정원|정부의, 의과대학)
# P(증원에|정부의, 의과대학, 정원) ~ P(증원에|정원, 예산)
#                                ~ P(정원, 예산, 증원에)/P(정원, 예산)
#                                ~ P(증원에|예산) -> P(예산, 증원에)/P(예산)
#                                                -> count(예산, 증원에)/N / count(예산)
#                                                -> count(예산, 증원에)/count(예산)

# P(F|A,B,C,D,E)

# Bigram -> Markov 1stAssumption
# Trigram -> Markov 2nd Assumption

# S => A, B, C, D, ... , Z
# P(S) => P(Z|A, B, ...Y)P(A, B, ...Y)
#      => P(Z|Y)P(Y|Z)P(X|W)..

# Ngram, Ngram Lanuage Model

def ngram(text, n=2):
    result = list()
    for i in range(len(text)-(n-1)):
        result.append(''.join(text[i:i+n]))
    return result

ngram('의대 교수 줄사직 시작됐다.'.split())

bigram = ngram(word_tokenize(corpus))
unigram = ngram(word_tokenize(corpus), 1)

bigramText = Text(bigram)
unigramText = Text(unigram)

unigramText.count('Emma')

unigramText.vocab().N()

unigramText.count('Emma')/unigramText.vocab().N()

unigramText.vocab().freq('Emma')

import re

def findToken(k, t):
    result = list()
    for token in t:
        if re.match(k, token):
            result.append(token)

    return result

for k in findToken, ('Emma', bigramText.tokens):
    print(k, bigramText.count(k)/unigramText.count('Emma'))

import re

def findToken(k, t):
    result = list()
    for token in t:
        if re.match(k, token):
            result.append(token)

    return result

netword = {k:bigramText.count(k)/unigramText.count('Emma')
    for k in findToken('Emma', bigramText.tokens)}

sorted(netword.items(), key=lambda r:r[1], reverse=True)[:5]



