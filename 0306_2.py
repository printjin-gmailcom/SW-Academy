# while, break, continue



a = 1

a = b = [1,2,3]

b[0] = 100

b[0]

a[0] #mutable data file 특징

b = a[:]

a[1] = 100

b

b = a.copy()

b

a,b=1,2 # 사실은 튜플

a

b

# unpacking

a,b = 1,2,3

a, *b = 1,2,3

a

b

*a = 1,2,3

*a, = 1,2,3

a



import builtins

dir(builtins)

for i in dir(builtins):
    if 'Error' in i :
        print(i)



a = 1
++a

a

a += 1

a

a = 3

b = 2

a, b = b, a

a



# ACCUMULATOR PATTERN

# 1 2 3 4 5 6
# 6 5 4 3 2 1

sum = 0
for i in range(1,11):
    sum = sum + i

sum

sum_ = 0
for i in range(1,11):
    sum_ = sum_ + i

sum_

del sum

sum_ = []
for i in range(1,11):
    sum_.append(i)

sum_

sum_ = []
for i in range(1,11):
    if i %2 == 0:
        sum_.append(i)

sum_

del sum_

a = [0,1,2,'',3,'a']

temp = []
for i in a:
    if not i:
        temp.append(i)

temp

any(a)

all(a)



a = input()

print(int(a)-2, '살입니다.')



a = 4

assert a == 1, 'a는 1이어야 한다.'

assert a == 4, 'a는 4이어야 한다.'



a = input()

b = int(a)

b

type(a)



while True:
    try:
        a = input('숫자를 입력하시오.')
        b = int(a)

    except ValueError:
        print('V')
        continue
    else :
        print('A')
        break





import sqlite3

con = sqlite3.connect('memory')

dir(con)



# 재사용 > declaration / definition
# - 함수
# - 클래스

# argument 아규먼트 (인자) : 사용
# parameter   파라미터 (매개변수) : 정의

def x(a):
    print(a)

x(3)

# 기본적으로 파라미터 수와 아규먼트 수 일치

def xx(a,b):
    print(a+2*b)

xx(2,3)

xx(a=2,b=3)

xx(b=2,a=3)

# default 값

# python 에는 기본적으로 function overloading 을 지원하는 않는 대신에, keyword 방식을 지원한다.

def xxx(a,b=3):
    print(a,2*b)

xxx(3)

xxx(3,4)

def xxx(a=3,b):
    print(a,2*b)



def xxxx(a, b=1, c=2, d=4): #한번 키워드 방식 쓰면 계속 키워드 방식 써야함.
    print(a,2*b)

xxxx(1,1,2,4)

xxxx(a=1, d=4)

xxxx(1, d=4)



def y(a,/,b):
    print(a,b)

def z(a,*,b):
    print(a,b)

y(1,3)

z(1,3)

y(a=1, b=3)

y(1, b=3)



len(obj[1,2,3])

obj = [1, 2, 3]
length = len(obj)
print(length)



import pandas as pd

pd.read.csv

import matplotlib.pyplot as plt

plt.hist

plt.hist([1,1,2,3,4,3])

plt.hist([1,1,2,3,4,3], color = 'pink')



def zz(*a): #가변 포지션널 방식
    print(a)

zz() #튜플 결과값

zz(1,)

zz(1,2,3,4)

zz(a=1)

def zz(**a): #가변 키워드 방식
    print(a)

zz() #딕셔너리 결과값

zz(1,)

zz(a=1)

zz(a=1, b=2, c=4)



def t(*a):
    print(a)

xx = [1,2,3,4]

t(xx)

t(*xx)



def tt(**a):
    print(a)

xxx = {'a':1, 'b':2}

tt(**xxx)



a = {'a':1, 'b':2}
c = {'a':3, 'c':4}

{**a, **c}



a = 1

t

a = t

aa = print

aa('문근영')

출력하다 = print

출력하다('ㅁ')

# 모든 것에 이름을 붙일 수 있음. 파이썬에서 변수라고 지칭할 수 없는 이유이다. 할당이 가능하기에.
# 근데 print = 1 같은 멍청한 짓은 금지

aa.__name__

aa.__qualname__



x # 파이썬에서는 이게 함수이다.
x()
x(a) # 함수가 아닌 리턴값
x(3)

x

x()

x(a)

x(3)



