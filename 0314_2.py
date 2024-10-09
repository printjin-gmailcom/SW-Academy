import torch

from torch.utils.data import Dataset

import inspect

print(inspect.getsource(Dataset))



# a = int 3 - JAVA,C의 경우

def sum_(a,b):
    return a + b

sum_('a','bbb')

# override 상속
# polymophism
# overloading - operator, function

def x(a):
    print(a)

def x(a,b):
    print(a,b)

def x(a,b=None):
    print('')

temp = []
for n in range(5):
    temp.append(lambda x, n=n : x+n)

temp

temp[1](3)



import seaborn as sns

iris = sns.load_dataset('iris')

iris

type(iris)

iris.describe()

iris['sepal_length'].describe()

type(iris['sepal_length'].describe())



class A:
    pass

class A(object, metaclass=type):
    pass



a = 1

type(a)

b = type(a)(3)

b

type(b)

# shift + tab

c = type('int2', (int,), {})

dir(c)

c(3)

#django metclass ;;;

# 간신분리 _ html, js, css 분리



# https://wikidocs.net/book/4170

# https://wikidocs.net/book/1



class A:
    def __init__(self,x):
        self.x = x

a = A(2)

A(2)

class A:
    def __init__(self,x):
        self.x = x
        return 1

a = A(2)

A(2)

class A:
    def __new__(self):
        print("new")
    def __init__(self,x):
        print("init")

a = A()

a

dir(type)

class A(metaclass=type):
    def __new__(self):
        print("new")
    def __init__(self,x):
        print("init")

a = A()

a

dir(type)

class A(metaclass=type):
    def __new__(cls):
        print("new")
        return super().__new__(cls)
    def __init__(self):
        print("init")

a = A()

int



from abc import ABCMeta, ABC, abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def x(self):
        pass

class B(A):
    pass

b = B()

class AA(metaclass=ABCMeta):
    @abstractclassmethod
    def x(self):
        pass

aa = AA()

from sklearn.naive_bayes import ABCMeta, GaussianNB

import inspect

print(inspect.getsource(GaussianNB))



a = [1,2,3,4,5]

[i+1 for i in a]

map(lambda x:x+1, a)

b = map(lambda x:x+1, a)

dir(b)

next(b)

next(b)

next(b)

next(b)

next(b)

next(b)

filter(lambda x:x>3, a)

c = filter(lambda x:x>3, a)

list(c)

# high other function



