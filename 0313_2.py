# assert



class A:
    x = 1
    y = 1

class B:
    x = 2

dir(A)

a = A()

dir(A)

sa = set(dir(a))

saa = set(dir(A))

sa - saa

sa ^ saa

class AA :
    def __init__ (self,x):
        self.x = x

aa = AA(3)

set(dir(aa))

set(dir(aa))-set(dir(AA))

# LEGB

aa.mro() # 가져다 쓸 수 없음. delegate 개념을 확실하게 알고 있기.

a.__class__

type(a)

b = [1,2,3]

b.__len__()

len(b)

dir(b)

b.__dir__()

a = [1,2,3]

a.append(4)

a

a.pop()

a

type(a)

type(list)

a.__bases__

list.__bases__

list.__base__

list.mro()

class A:
    def x(self):
        self.x = 1
        print('x')

class B:
    def y(self):
        self.y = 2
        print('y')

class C:
    def __init__(self):
        self.a = A()
        self.b = B()
    def cc(self):
        self.a.x()
        self.b.y()

c = C()

c.cc()



class A:
    x = 1
    def y(self):
        print('y')

class B(A):
    pass

class C:
    def __init__(self):
        self.a = A()

b = B()

b.x

c = C()

c.X

class C:
    def __init__(self):
        self.a = A()

    def __getattr__(self,x):
        print(x)

c = C()

c.x

getattr(-1, '__abs__')()

a = input()

getattr(-1,a)()

1.__getattribute__('__abs__') #1.은 float라서

1 .__getattribute__('__abs__')

(1).__getattribute__('__abs__')

a = 1

a.__getattribute__('__abs__')

a.__getattribute__('__abs__')()

class C:
    def __init__(self):
        self.a = A()

    def __getattr__(self,x):
        return getattr(self.a,x)

c = C()

c.x

c.y()



from sklearn.naive_bayes import GaussianNB, BernoulliNB, CategoricalNB



def get_primes():
    "Simple lazy Sieve of Eratosthenes"
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

from collections.abc import Sequence

class ExpandingSequence(Sequence):
     def __init__(self, it):
         self.it = it
         self._cache = []
     def __getitem__(self, index):
        while len(self._cache) <= index:
             self._cache.append(next(self.it))
        return self._cache[index]
     def __len__(self):
         return len(self._cache)

primes = ExpandingSequence(get_primes())

for _, prime in zip(range(10), primes):
    print(prime, end=" ")



from collections.abc import Sequence

class ExpandingSequence(Sequence):
     def __init__(self, it):
         self.it = it
         self._cache = []
#     def __getitem__(self, index):
#        while len(self._cache) <= index:
#             self._cache.append(next(self.it))
#         return self._cache[index]
     def __len__(self):
         return len(self._cache)

primes = ExpandingSequence(get_primes()) # 똑같이 다 있어야 실행된다



from abc import abstractmethod

class ExpandingSequence:
     def __init__(self, it):
         self.it = it
         self._cache = []

@abstractmethod
def __getitem__(self, index):
    raise NotImplemmentedError

def __len__(self):
    return len(self._cache)

class X(ExpandingSequence):
    pass

x = X(get_primes())

x[0]



import tensorflow as tf

import inspect

print(inspect.getsource(tf.keras.utils.Sequence))



# 상속
# duck typing
# composition

# 추상화 > 필수적인 공통된 강제
# - duck typing
# - 상



from collections.abc import Sequence

class A(Sequence):
    pass

a = A()

from abc import abstractmethod

class B:
    @abstractmethod
    def __getitem__(self,x):
        raise NotImplementedError

class C(B):
    pass

c = C()

c[0]

class D(B):
    def  __getitem__(self,x):
        return [1,2,3]

d = D()

d[0]



def x():
    ...



from collections.abc import Iterable, Iterator

# protocol
# iterable __iter__
# itertator __iter__, __next__





# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

import torch

from torch.utils.data import Dataset

import inspect

print(inspect.getsource(Dataset))



