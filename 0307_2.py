def x():
    print('a')
    return None

def x():
    print()

type(x)

b = [x]

b[0](4)



# first class
# higher order : 함수를 인자로 사용하고 리턴할 수 있는 함수



# 1 3 5 7 9 as_1 = an + 2 a1 = 1

def t(x):
    if x == 1:
        return 1
    return t(x-1)+2

t(3)



b = 1
def a():
    return b

a()

b = 1
def a():
    ttt = 3
    return b

a()

ttt #접근제한, scope



#Logcal Encrossing Global Bulit-in

globals()



b = 1
def a():
    ttt = 3
    b = 2
    return b

a()



b = 1
def a():
    ttt = 3
    b = 2
    return b

def aa():
    b=3

a()



sum = 0 #builtins : sum

sum

del sum

sum

# incapsulation



# Commented out IPython magic to ensure Python compatibility.
# %timeit
temp = []
for i in range(1000000):
    temp.append(i)
temp

# Commented out IPython magic to ensure Python compatibility.
# %timeit
temp = [i for i in range(100000)]



# 여러개의 값을 쉽게 만들거나, 변화 시킬때 사용

[i for i in range(10)]

i



a = [i for i in range(10)]

[b+1 for b in a]

[b for b in range(10) if b%2==0]

[b if b%2 ==0 else '' for b in range(10)]

[(a,b) for b in range(10) for a in range(11,20)]



import antigravity

a = 1
a = ' ' # 재할당

id(a)

a = 1000
b = 1000

a,b

id(a), id(b)

a = 256
b = 256

id(a), id(b) # 자주 사용하는 숫자는 픽스 interning

a == b

a is b

import sys

sys.intern('a')

a = 1

id(a)

a = 2

id(a)



x = [1,2,3]

id(x)

x.append(4)

id(x)

x

y = x

id(y)



aa = [1,2,3]

aa = {'a':1}

aa['b']

aa['b'] = 2

aa



(i for i in  range(10))



# 앞에서부터 (iterable 중간단계) (interator : 사용자 편의성)
# iterable == generator 친척 관계, 만드는 방식이 다르고 같은 역할을 함



sum

def y():
    print('y')
    return print

import dis #disassemble,Python 인터프리터가 사용하는 바이트 코드(bytecode)를 분석하여 출력하는 모듈. 함수나 메서드의 바이트 코드를 확인 가능.

dis.dis(y)



a = [1,2,3]

b = iter(a) # 숨겨진 기능

next(b)

next(b)

next(b)

next(b)



c = (i for i in range(10))

c



def z():
    yield 1
    yield 2

zz = z()

zz

next(zz)



# 데이터 -> 1개씩 추출 위해서



# higher order function



# list
# tuple
# set
# frozenset

from collections import namedtuple, OrderedDict



def y():
    print('y')
    return print

# y() ~ 함
# y()()() ~ 불가능
# 함수를 리턴한다는 의미



