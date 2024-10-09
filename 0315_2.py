# AOP ~ 관점에 따라 객체 지향 넓히는 개념
# 상속 -- 다중 상속
# django mixins
# decorator
# tensorflow -- tf.function

# def foo():
#     print('foo!')
# #   return None ~ 생략가능


# def bar(fn):
#     fn(# __call__# ) ~ 생략


# def foo()
#     def bar():
#         print('bar!') #closure와 같은 특수 기능
#     bar()

# ctrl + fn

a = 1
def x():
    return a

x()

a = 1
def x():
    a = a+1
    return a

x() #UnboundLocalError

a = 1
def x():
    global a
    a = a+1
    return a

x()

a # 이런 상황때문에 global 자제하도록 함

a = 1
def xx():
    a = 1 #encloding
    def xxx():
        return a
    return xxx()

xx()

a

a = 2

def xx():
    a = 1 #encloding
    def xxx():
        nonlocal a
        a = a+1
        return a
    return xxx()

xx()

def y(m):
    def z(n):
        return m+n
    return z

class A:
    def __init__(self,m):
        self.m = m
    def __call__(self,n):
        return self.m + n

A(2)(4)

# model 안에서 __call__이 정의 되어있음.
# def __call_(self):
#    self.build()
#    self.call()

class A(model): # model 상속
    def __init__(self,m):
        self.m = m
    def __call__(self,n):
        return self.m + n

# function closure
# decorator

def t(fun):
    def s():
        print('---')
        fun()
        print('---')
    return s

t(print)

t(print)()

t(lambda : 1)

t(lambda : 1)()

def ss():
    print(ss)

t(ss)()

def ss():
    print('ss')

t(ss)()

@t #단축표현, ss함수를 t함수에 집어넣어서 결과값을 낸다는 의미, 새로운 정수를 만들어준다. syntatic sugar
def ss():
    print('ss')

ss()

# 파이썬에서는 다중상속으로 가능, high-other-function

# https://spoqa.github.io/

from functools import partial

from operator import add

add(3,4)

add(3,5,6)

add3 = partial(add,3)

add3(4)

ss

# decorator을 만드는데 decorator를 활용

from functools import wraps

def t(fun):
    @wraps(fun)
    def s():
        print('---')
        fun()
        print('---')
    return s

@t
def ss():
    print('ss')

ss

# wrap을 안쓰면 local이 뜨고 사용하면 이름이 달라짐

def x(m):
    def y():
        print('y')
    return y

x

x(1)

x(1)()

def x(a):
    print(a)

def xx():
    print('a')

def tt(fun):
    def ss():
        print('xxx')
        fun()
    return ss

@tt
def x(a):
    print(a)

x(3) # 인자 맞추기 게임

def tt(fun):
    def ss(b):
        print('xxx')
        fun(b)
    return ss

@tt
def x(a):
    print(a)

x(3)

@tt
def xx():
    print('a')

xx()

def tt(fun):
    def ss():
        print('xxx')
        fun()
    return ss

@tt
def xx():
    print('a')

xx()

int

def tt(fun):
    def ss(*args, **kwargs):
        print('xxx')
        fun(*args, **kwargs)
    return ss

@tt
def xx():
    print('a')

xx()

# *args, **kwargs ~ 세상의 모든 인자 문제에서 벗어날 수 있음. 꼭 친해지기

# __new__

# @tf.function
# @tf.function() - 함수형 패러다임 때문
# @function.tools.

# 파이썬에서 삼중구조를 최대로 하기를 추천, 이상 사용할 수는 있으나 자제

def x(*a):
    return a

x()

def x(**a):
    return a # 딕셔너리

x()

x(a=3)

def x(**a, *b):
    return a

def x(*a, **b):
    return a

x(a=3)

# map

def x(fun):
    def y(*a, **b):
        print('---')
        fun()
        print('---')
    return a

def s(n):
    def x(fun):
        def y(*a, **b):
            print('---')
            fun(*a, **b)
            print(n)
            print('---')
        return a

@s
def yyy():
    print('ttt')

yyy()

@s(3)
def yyy():
    print('ttt')

yyy()

def s(n):
    def x(fun):
        def y(*a, **b):
            print('---')
            fun(*a, **b)
            print(n)
            print('---')
        return s

@s(3)
def yyy():
    print('ttt')

yyy()

def s(n):
    def x(fun):
        def y(*a, **b):
            print('---')
            fun(*a, **b)
            print(n)
            print('---')
        return x
    return s

@s(3)
def yyy():
    print('ttt')

yyy()

def x(fun):
    def y(*a, **b):
        print('---')
        fun(*a, **b)
        print('---')
    return y

@x
def yyy():
    print('ttt')

yyy()

def s(n):
    def x(fun):
        def y(*a, **b):
            print('---')
            fun(*a, **b)
            print('---')
        return y
    return x

@s
def yyy():
    print('ttt')

yyy()

def s(n):
    def x(fun):
        def y(*a, **b):
            print('---')
            fun(*a, **b)
            print('---')
        return y
    return x

@s(3)
def yyy():
    print('ttt')

yyy()

# decorator을 감싸는 경우는 인자를 하나 더 받을 수 있음
# @ 일때 ( ) 을 붙여야

def s(n=1):
    def x(fun):
        def y(*a, **b):
            print('---')
            fun(*a, **b)
            print('---')
        return y
    return x

@s()
def yyy():
    print('ttt')

yyy()

# =이 붙으면 @ 일때 () 로 표시해도 가능



import torch

from torch.utils.data import Dataset

import inspect

print(inspect.getsource(Dataset))



# PuTTY # https://www.putty.org/

