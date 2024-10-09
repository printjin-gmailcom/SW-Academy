import numpy as np

a = np.array([1,2,3,])

b = a

b[0] = 100

b

a

a = np.array([1,2,3,])

b = a.copy()

b[0] = 123

b

a

x = [[1,2],[3,4]]

y = x.copy()

y[0][0] = 100

x

y

# copy - deep, shallow

import copy

y = copy.deepcopy(x)

y[0][0] = 1

y

x

# numpy nd_array

xx = np.array([[1,2],[3,4]])

yy = xx.copy()

yy[0][0] = 100

yy

xx

# numpy의 copy는 기본 deepcopy
# shallowcopy를 원한다면 view 사용

yyy = xx.view()

yyy

yyy[0][0] = 123

yyy

xx

# tensorflow ~ check point

xx

xx[0][0] = 1

xx

x[0][0]

# index와 slicing은 copy개념은 아님

a = np.arange(24).reshape(4,6)

a

a[1]

a[1][:]

a[1,:]

a[[1]] # fancy indexing

a[[2,1]] # 재조합은 copy

import seaborn as sns

tips = sns.load_dataset('tips')

tips

tips[['total_bill', 'tip']]

tips[['tip' , 'total_bill']]

a

a[0,2], a[1,1]

a[(0,1),(2,1)]

a[(0,1,-1),(2,1,-3)]

a[[0,1,-1],[2,1,-3]] # iterable

...

a[None]

aa = np.arange(24).reshape(2,3,4)

aa

aa[:,:,0]

aa[:,1,:]

aa[:,:,0]

aa[...,0]

dir(tips)

# spicy > ndimage > spicy-toolkit
#       > ml       > scikit-learn



