# https://docs.python.org/ko/



a = 1

a



# _ : snake
# moon_beauty
# moonBeauty : 카멜 방식
# MoonBeauty : 파스칼 방식



from tensorflow.keras import Sequential

from sklearn.datasets import *



import keyword

keyword.kwlist

len(keyword.kwlist)



import sys

sys.maxsize



sys.float_info



a = 1.98378923e+308

a



a == a+1



1e2



#리터럴 (literal) - 리터럴이 안붙는 정수는 10진수밖에 없음

0b01 #0b 이진수

0b03

0x01 #0x 8진수

0x08



.3

3.

3e3

inf

float('inf')



3 + 4j #복소수 ~ 복소평면



True

True + 1

False

False + 3

issubclass(bool, int)

type(True)



float('nan')



3/7

3//7

3%7

7/-3 #= -3 + 0.66666

7//-3

7 % -3

-7 % 3



7 + 0.3 #coercion(코어션)(묵시적 형변환)



b'asb'

b'ㄱㄴㄷ'

u'ㄱㄴㄷ' #유니코드



1000 #atom - 더 이상 쪼개지면 안되는 것, 숫자. 쪼개기 위해서는 _ 사용

10_000_000_000



len('abc')



#container ~

# 시퀀스 ~ 순서가 있는 컨테이너
# 문자는 대표적인 시퀀스 데이터 컨테이너
# 순서가 중요하며 각각의 요소가 중요



'abc'*3



type(3)

type(True)

type('bc')

type(b'bc')

# iterable



c = 100

c

c[0]

c = 'abc'

c[1:]

c = 'abc' + 'def'

c

c = 'abc' + 3



import numpy as np

a = np.array([1,2,3.])

a



import tensorflow as tf

tf.constant([1,2,'3'])



a = [1,2,3]

a

a*3



1,2

a = 1,2,3

a

a = {1, 2}

a

# 집합, 순서 사용자가 정의 불가능.

type(a)

b = {}

b

type(b)

set() # 공집



b = {'a':1}

b

a = {3, '1', [1,2,3]}



import this



value : data type + data #type의 중요시



# 조건문은 존재론적인 관점에서 따진다

a = 1
if a :
    print('a')
else :
    print('b')

a = ''
if a :
    print('a')
else :
    print('b')

a = 0 #존재론적으로 없음으로 인정
if a :
    print('a')
else :
    print('b')

if a :
    print('a')
else :
    print('b')

a = list()
if a :
    print('a')
else :
    print('b')

if float('nan'):
    print('a')
else :
    print('b')



# literal
# instance

a = int(3)

a

type(a)

a = int()

a

type(a)



for i in 1,2,3:
    print(i)

for i in 1,2,3:
    print(i)
else :
    print('end')

try:
    1
except:
    print('a')
else:
    print('b')



False == None

if None :
    print('a')
else:
    print('b')



import keyword

# as, else, from



3 > 1.0

'a' > 'A' #문자의 경우 가능 (97>65)

'a' > 'Aa' #시퀀스는 맨 앞자리에서 대수가 결정나면 뒤에는 안봄 = short circuit

[1,2] > [3]

1,2,3 > 3 # 연산자 우선순위로 1,2,(3>3)으로 계산

(1,2,3) > (3,)

{3,2,1} > {3} # set은 시퀀스가 아니라 (1,2,3) 으로 자동 정리.



3 and 4 # 앞이 참이면 뒤를 반환, 앞이 거짓이면 앞을 반환

'' and 4

3 or 4 # 앞이 참이면 앞을 반환, 앞이 거짓이면 뒤를 반환

'' or 4

3 or 4/0 # 앞이 참이면 앞을 반환, 앞이 거짓이면 뒤를 반환

3 and 4/0



3 if 4 else 1 # 삼항연산자 # 조건

3 if 0 else 1



# for
# while

help('in')

1 in 100

1 in [1,2,3,4]

a = 1

if a == 1 or a == 2 or a == 3:
    print('x')

import this

a = 1
a not in [1,2,3]

a = 1
a not in 'a,b,c,d'

a = 1
'2' in 'a,b,c,d'

# iterable가 python에서 iterator로 변화



# duck typing : 오리처럼 보이고 오리처럼 행동한다면 그것은 오리다. ~ tensorflow pytorch에서도 많이 활용

from collections import Iterable



a = 1

dir(a)

a = [1,2,3]

dir(a)

'__iter__' in dir(a)

for i in a :
    print(i)



import seaborn as sns

tips = sns.load_dataset('tips')

tips

for i in tips:
    print(i)



# all(), any(), enumerate() ~ itierable



for i in {'a':1, 'b':2, 'c':3}:
    print(i)

{'a':1, 'a':2, 'c':3} #reassignment

1 in {'a':1, 'b':2, 'c':3} #dic에서는 key가 중요

for i in {'a':1, 'b':2, 'c':3}.keys(): #dictionary view
    print(i)

for i in {'a':1, 'b':2, 'c':3}.values(): #dictionary view
    print(i)

for i in {'a':1, 'b':2, 'c':3}.items(): #dictionary view
    print(i)



class A:
    a = 1

aa = A()

for i in aa:
    print(i)

class A:
    a = 1
    def __iter__(self):
        return iter([1,2,3])

aa = A()

for i in aa:
    print(i)



