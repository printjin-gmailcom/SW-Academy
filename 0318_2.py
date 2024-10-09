# paperwithcode

# https://logseq.com/



# data, data type, value

# literal, instancee, factory method

# Homogeneous sequence data type



import array

array.array

a = array.array('B',[1,2,3])

a

a[0]

a' = array.array('B',[-1,2,3])

b = array.array('B',[1,2,3])

b

a + b

class A:
    def __add__(self,x):
        print('add')
        return 0

a = A()

a

a + 1

# operator overloading



# https://matplotlib.org/



# vectorized



import numpy as np

a = np.array([1,2,3])

a

type(a)

import tensorflow as tf

b = tf.constant([1,2,3])

type(b)



import seaborn as sns

t = sns.load_dataset('tips')

dir(t)



b = tf.constant([1, '1'])

a = np.array([[1,2],[3,4]])

a

a = np.array([[1,2,3],[3,4,5]])

a

a.shape

a.ndim

a.dtype

b = tf.constant([1, 1])

b



x = tf.keras.datasets.mnist.load_data()

x

len(x)

x,y = tf.keras.datasets.mnist.load_data()

x

y

len(x), len(y)

(x,y), (z,u) = tf.keras.datasets.mnist.load_data()

(x,y)

x.shape



# descriptor



tips = sns.load_dataset('tips')

tips

tips.size

dir(tips)



a.itemsize



# numpy에서는 1열로 저장 ~ stride 기능



a = np.arange(24).reshape(2,3,4)

a

a = np.arange(24).reshape(3,2,4)

a



