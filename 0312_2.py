# 메모리 실행이 가장 빠르면 먼저 실행
# 그게 안되면 가상 메모리가 만들어져서 실행
# 그럼에도 안되면 에러가 뜬다



a = [1,2,3,4]

dir(a)

a[3]

b = iter(a)

b[0]

next(a)

next(b)

b

list(b)

next(b) #StopIteration:

dir(b)

for i in [1,2,3]:
    print(i)



# class, meta class, instance
# type = class



a = 1

type(a)

aa = int(1)

aa, type(aa)

type(int)

type(type)

# type 은 최상위에 있음. metaclass로 봄.

# 함수에 대응하는 magic/special or dundu (double underbar) 있을 수 있

a = [1,2,3]

len(a)

type(a)

a.__class__ #pythonic

a.__len__

# method가 있으면 함ㅁ수가 있음. 역은 성립하지 않음.



class A:
    pass

a = A()

a.x = 1

vars(a)

a.__dict__

vars(A)

A.__dict__

import sys

sys.getrefcount(a)

import gc



class B:
    '''설명할께요'''
    pass

def t():
    '''설명 안할래'''
    pass

b = B()

def tt():
    '''Return the number of items in a container'''
    pass



"" 4:14 내외 한 두번째 강의 30분 내 ""

class C:
    def t(self):
        pass

C.t

cc = C()

cc.t



# 상속 : 남이 만든거 가져다가 나에게 맞춘다
# - 추가, 변경 삭제

# 단일 상속, 다중 상

class D:
    pass

dir(D)

class D(object):
    pass

class D(object, A):
    pass

class A:
    x = 1
    y = 2

A

class B(A):
    pass

b = B()
b.x



b.x is A.x # 인스턴스 없으면 클래스 찾아간다. deligate ~ 파이썬 디자인 패턴



class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(B,C): # method resolution order (MRO) - 메소드 실행 순서 에러
    pass

class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C, B):
    pass

D.mro()

dir(type)

# overriding

a = 1
a = 2

a

a = 1
a = 2

def a():
    print('a')

a()



class A:
    t = 1
    def x(self):
        print('x')

A.x



class B:
    def x(self):
        print('xx')

b = B()

b.x()



class B(A):
    def x(self):
        A.x(self)
        print('xx')

bb = B()

bb.x()



class B(A):
    def x(self):
#       A.x(self)
        super().x() # super 매우 중
        print('xxx')

bbb = B()

bbb.x()



class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')

class C(A):
    def __init__(self):
        print('C')

class D(B,C):
    def __init__(self):
        print('D')

D.mro()

d = D()



class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        A.__init__(self)
        print('B')

class C(A):
    def __init__(self):
        print('C')

class D(B,C):
    def __init__(self):
        B.__init__(self)
        print('D')

d = D()

class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        A.__init__(self)
        print('B')

class C(A):
    def __init__(self):
        print('C')

class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('D')

d = D()

class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(A):
    def __init__(self):
        super(C,self).__init__()
        print('C')

class D(B,C):
    def __init__(self):
        super().__init__()
        print('D')

d = D()

D.mro()



class A:
    def __getitem__(self, x):
        print('get item')
    def __len__(self):
        print('len')
        pass

class A:
        pass

a = A()

a[0]



class A:
    def __getitem__(self, x):
        print('get item')

a = A()

a[0]

a[-3]

len(a)

class A:
    def __getitem__(self, x):
        print('get item')
    def __len__(self):
        return 0

a = A()

a[-3]

len(a)



from collections.abc import Sequence

class A(Sequence):
    def __getitem__(self, x):
        print('get item')
    def __len__(self):
        return 0

a = A()

a[-3]

len(a)



import tensorflow as tf

import inspect

print(inspect.getsource(tf.keras.utils.Sequence))



