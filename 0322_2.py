# https://lectures.scientific-python.org/
# https://github.com/rougier/numpy-100
# https://www.labri.fr/perso/nrougier/from-python-to-numpy/

import tensorflow as tf

a = tf.constant([1,2,3])

dir(a)

!pip install spicy

from spicy import stats

dir(stats)

stats.beta



import numpy as np

a = np.arange(24)

a

a.reshape(2,3,4)

a

b = a.reshape(2,3,4)

a

b

b[0,0,0] = 100

b

a

b = a.reshape(2,3,4)

b

b = a.reshape((2,3,4))

b

np.reshape(a, (2,3,4))

a.reshape(3,6)

a.reshape(3,-1)

a.reshape(3,-2)

a.reshape(3,-3)

a.reshape(2,-1,1)

a

import numpy as np

b = np.resize(a, (2,6))

print(b)



import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split



b = a.flatten()

b

b[0] = 1

b



a.ravel()

# 뷰 = 볼레로



aa = np.arange(6).reshape(2,3)

aa

aa[None]

aa[:, None]

aa[...,None]

aa[:,:,None]

aa[np.newaxis]

aa[np.newaxis] is None



from collections import namedtuple

Point = namedtuple('Point', 'x y')

p1 = Point(x=3, y=4)

p1.x

p1[0]

import sys

sys.float_info

# reshape
# - flatten / ravel
# - [None]

x = np.array([('Rex', 9, 81.0),('Fido', 3, 27.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('wight', 'f4')])

x

x[0]

x['name']

x.name

xx = np.rec.array([('Rex', 9, 81.0),('Fido', 3, 27.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('wight', 'f4')])

xx

xx.name

xxx = np.ma.array([1,2,3])

xxx

xxx = np.ma.array([1,2,3], mask=[True, False, True])

xxx

xxx.count()

xxxx = np.matrix([[1,2],[3,4]])

xxxx

xxxx = np.mat([[1,2],[3,4]])

xxxx

xxxx*xxxx

from functools import reduce

reduce(lambda x, y:x+y, [1,2,3,4,5])

a = np.arange(6).reshape(2,3)

a

a.strides

a.itemsize

a.dtype

a.sum(axis=0)

a.sum(axis=1)

aa = np.arange(24).reshape(2,3,4)

aa

aa.sum(axis=None)

aa.sum(axis=0)

aa.sum(axis=1)

aa.sum(axis=2)



# flatten - copy vector



# data-science ; unicorn



# 파일 형식
# - 텍스트 : human-readable, byte



# Commented out IPython magic to ensure Python compatibility.
# %%writefile a.txt
# 1 2 3
# 4 5 6
# 6
# 7

a = open('a.txt')

dir(a)

a.readline()

next(a)

a.close()



class D:
    pass

d = D()

with d:
    pass

class D:
    def __enter__(self):
        print('enter')

d = D()

with d:
    pass

class D:
    def __enter__(self):
        print('enter')
    def __exist__(self):
        print('exit')

d = D()

with d:
    pass

class D:
    def __enter__(self):
        print('enter')
    def __exit__(self, a, b, c):
        print('exit')

d = D()

with d:
    pass

dir(d)

import sqlite3

b = sqlite3.connect(':memory:')

with b:
    pass

dir(b)

import pickle #직렬화

a = [1,2,3]

with open('b.txt', 'w') as f:
    f.write(a)

with open('b.txt', 'wb') as f:
    pickle.dump(a,f)

with open('b.txt', 'rb') as f:
    xx = pickle.load(f)

xx

type(xx)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile c.txt
# 1 2 3
# 4 5 6

c = np.loadtxt('c.txt')

c

type(c)

np.save('c')

np.save('c.npy', c)

np.savez('c.npy', c)

np.load('c.npy')

np.loadtxt('c.txt')

c

np.save('c.npy', c)



import inspect

print(inspect.getsource(tf.keras.datasets.mnist.load_data))

