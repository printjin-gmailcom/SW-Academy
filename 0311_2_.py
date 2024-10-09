a = int(1)

b = int(2)

c = int(3)



# 함수 : 정의, encapsulation, LEGB
# 클래스 : encapsulation, 접근 제한 없음 - discriptor

class A:
    pass

a = A()

a.x = 1

a.x

class A:
    x = 1
    def xx(self):
        print('a')

class A:
    x = 1
    def xx(self, t):
        self.t = t
        print(self.t)

# attribute
# method
# class variation
# instance variation

a = A()

a.x = 1

a.x

a = 1 # literal
a = int()

class int:
    pass

a = list()

dir(a)

# class = data type + 행동까지 정의

a.app



class A:
    x = 1

a1 = A()
a2 = A()
a3 = A()

a1.t = 3
a2.t = 4
a3.t = 'a'

a1.x

a2.x

# instance 변수는 method가 실행 후 생성

class B:
    def bb(self):
        self.t = 1

b = B()

vars(b)

dir(b)

b.bb()

vars(b)

dir(b)

class C:
    def __init__(self):
        print('A')

c = C() #operator overloading, constructor, magic method

class D:
    def xx(self,x):
        self.x = 1
    def xxx(self):
        print(self.x)

dd = D()

vars(dd)

# instance 변수는 첫번째 인자를 생략하고 메소드 사용

dd.xx(1)

vars(dd)

dd.xxx()

#instance 변수는 instance 내에서 공유됨
#class 변수는 instance 간에 공유됨

class D:
    def __init__(self):
        print('A')
    def xx(self,x):
        self.x = 1
    def xxx(self):
        print(self.x)



a = 1

def x():
    print(a)

def xx():
    print(a+)

class X:
    a = 1

def x(self):
    print(a)

def xx(self):
    print(a+)

class X:

    def x(self, x):
        self.x = x
        print(self.x)

    def xx(self):
        print(self.x)

X.x

a = X()
X.x(a,3)

class X:

    def t(self, x):
        self.x = x
        print(self.x)

    def tt(self):
        print(self.x)

X.t

a.t

# 공유 (instance, class)

# len

# int



# instance화 하지 않고 class 자체 사용 가능 (metaclass 존재)

class T:
    def __init__(self):
        self.a = 1
        print("init")

t = T()

t()

class TT:
    def __init__(self):
        self.a = 1
        print("init")
    def __call__(self):
        print('call')

tt = TT()

tt()

class S:
    def __init__(self, a):
        self.a = a
        print("init")
    def __call__(self, b):
        return self.a
        print('call')

S(1)

S(1)(4)



import tensorflow as tf

ss = tf.keras.utils.Sequence

dir(ss)



# static method

class T:
    @staticmethod
    def ss():
        print('static')

T.ss()

t = T()
t.ss()

t

t = TT()

t.ss()

class T:
    @staticmethod
    def ss(ㅁ):
        print('static')

T.ss(1)

t = T()

t.ss(1)

t.ss()



def sin(self):
    print('x')

class MATH:
    def sin(self):
        print('x')
    def cos(self):
        []

A.x

class T:
     x = 1

t = T()

t.x

vars(t)

t.x = 2

vars(t)

t.x

s = T()

s.x



class Y:
    @classmethod
    def z(cls):
        cls.x = 1

Y.z()

class Y:
    @classmethod
    def z(cls):
        cls.x = 1
        print('cls')

yy = Y()

yy.z()

yy.x

vars(yy)



import pandas as pd

pd.DataFrame.from_dict

len({'a':1})

# 같은 함수 또는 메소드 타입에 따라 다르게 행동한

# generic

from functools import singledispatch

@singledispatch
def x(a):
    print(a)

@x.register(int)
def _(a):
    print('int')

@x.register(str)
def _(a):
    print('str')

x(3.)

x(3)

# is
# callable > True, False : predicate

isinstance(3, int)

issubclass(bool, int)



