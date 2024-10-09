import numpy as np

a = np.array([1,2,3])

a.shape

a.dtype

class A:
    __x = 1

dir(A)

A._A__x

class B:
    pass

class C:
    b = B()

class B:
    pass

class C:
    bb = B()
    def __init__(self):
        self.b = B()

C.bb

class B:
    def __get__(self):
        print('get')

class C:
    bb = B()
    def __init__(self):
        self.b = B()

C.bb

class B:
    def __get__(self, a, b):
        print('get')

class C:
    bb = B()
    def __init__(self):
        self.b = B()

C.bb

class B:
    def __get__(self, a, b):
        print('get')
    def __set__(self,x):
        print('set')

class C:
    bb = B()
    def __init__(self):
        self.b = B()

C.bb

C.bb = 3

C.bb

C.bb

dd = C()

dd.bb

class B:
    def __get__(self, a, b):
        print('get')
    def __set__(self,x):
        print('set')
        return 1

class C:
    bb = B()
    def __init__(self):
        self.b = B()

cc = C()

cc.bb

vars(cc)

cc.bb = 3

cc.bb

a = np.array([1,2,3,4])

a

a.shape = (2,2)

a

import tensorflow as tf

x = tf.constant([1,2,3,4])

x

x.shape = (2,2)

class D:
    def g(self, x, y):
        print('get')
    x = property(g)

d = D()

d.x

class D:
    def g(self):
        print('get')
    def s(self):
        print('set')
    x = property(g)

d = D()

d.x

class D:
    def g(self):
        print('get')
    def s(self):
        print('set')
    x = property(g, s)

d = D()

d.x

d.x = 1

class D:
    def g(self):
        print('get')
    def s(self):
        print('set')
        return 3
    x = property(g, s)

d = D()

d.x

d.x = 1

d.x

class D:
    def __init__(self):
        self.m = 0
    def g(self):
        print('get')
        return 3
    def s(self):
        print('set')
    x = property(g, s)

d = D()

d.x

d.x = 2

d.x

class D:
    def __init__(self):
        self.m = 0
    def g(self):
        print('안알려줌')
        return 3
    def s(self, t):
        print('set')
    x = property(g, s)

d = D()

d.x

class D:
    def __init__(self):
        self.x = 0
    def g(self):
        print('안알려줌')
        return 3
    def s(self, t):
        print('set')
    x = property(g, s)

d = D()

d.x

d.x = 5

d.x

class D:
    def __init__(self):
        self.x = 0
    def g(self):
        print('알려줌')
        return x
    def s(self, t):
        print('set')
    x = property(g, s)

d = D()

d.x

class D:
    def __init__(self):
        self.__x = 0
    def g(self):
        print('알려줌')
        return __x
    def s(self, t):
        print('set')
        self.__x = t
    x = property(g, s)

d = D()

d.x

d.x = 5

d.x

class D:
    def __init__(self):
        self.__x = 0
    def g(self):
        print('알려줌')
        return self.__x
    def s(self, t):
        print('set')
        self.__x = t
    x = property(g, s)

d = D()

d.x

d.x = 5

d.x

class E:
    def __init__(self, x):
        self.x = x

    def t(self):
        return self.x

d = E(3)

d.t()

class E:
    def __init__(self, x):
        self.x = x

    @property
    def t(self):
        return self.x

d = E(3)

d.t()

class E:
    def __init__(self, x):
        self.__xx = x

    @property
    def x(self):
        return self.__x

d = E(3)

d.t()

class E:
    def __init__(self, x):
        self.__xx = x

    @property
    def x(self):
        return self.E__x

d = E(3)

d.t()

class E:
    def __init__(self, x):
        self.__xx = x

    @property
    def x(self):
        return self.E._E__x

d = E(3)

d.t()

class E:
    def __init__(self, x):
        self.__xx = x

    @property
    def x(self):
        return self.__xx

d = E(3)

d.x

class E:
    def __init__(self, x):
        self.__xx = x

    @property
    def x(self):
        return self.__xx

    @x.setter
    def x(self,x):
        print('set')
        self.__x = x

d = E(3)

d.x

d.x = 5

d.x

class E:
    def __init__(self, x):
        self.__xx = x

    def x(self):
        return self.__xx

d = E(3)

d.x

d.x()

import numpy as np

a = np.array([1,2,3,4])

a.ndim = 2

a.ndim

a.ndim()

import seaborn as sns

tips = sns.load_dataset('tips')

tips

a = np.zeros((3,4))

a

a = np.identity(4)

a

a = np.eye(3,4)

a

a = np.triu(3)

a = np.triu((3,4))

a

np.ones_like(a)

import tensorflow as tf

tf.ones((3,4))

np.lookfor('triangle')

np.info('tril')

# absolute basic

a = 3

a

print(a)

class A:
    def __str__(self):
        print('str')
        return 1
    def __repr__(self):
        print('repr')
        return 2

x = A()

x

class A:
    def __str__(self):
        print('str')
        return '1'
    def __repr__(self):
        print('repr')
        return '2'

x = A()

x

print(x)

a = np.array([1,2,3,4])

print(a)

import inspect

inspect.getsource(A)

from sklearn.datasets import load_iris

data = load_iris()

print(data.DESCR)

a = tf.constant([1,2,3])

a

print(a)

import pprint

pprint.pprint(a)

import this

a = np.array([1,2,3])
b = np.array([1,2,3])

# elementwise ~ 원소별로 하기

a + b

a * b

a ** b

# class X:
#     def __add__(se)

from operator import add

a = np.array([1,2,3])
b = np.array([2,3,1])

np.dot(a,b)

# type __class__

a.dot(b)

# 연산자가 있으면 함수 또는 메소드 존재한다

a@b

aa = np.array([[1,2],[3,4]])
bb = np.array([[1,2],[3,4]])

aa@bb

aa.dot(bb)

# broadcasting

a

a + 1

aa = np.array([[1,2],[3,4]])

aa + 1

aa + np.array([[1,2]])

aa + np.array([[1,2,3]])

tf.constant([[1,2]]) + tf.constant([[1],[2]])

tf.constant([[1,2,3]]) + tf.constant([[1,2],[2,3]])

a = np.arange(24).reshape(4,6)

a

a[0][2]

a[0,2]

a = np.arange(24).reshape(2,3,4)

a[0][1][2]

a[0,1,2]

import seaborn as sns

tips = sns.load_dataset('tips')

tips

tips.iloc[2]

tips.iloc[2,1] = 100

tips

# comma indexing
# boolean indexing

b = np.array([1,2,3,4])

b[True, True, False, True]

b[(True, True, False, True)]

b > 2

b[b>2]

tips[tips.sex == 'Male']



