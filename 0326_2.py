# 경찰청_범죄 발생 지역별 통계_20151231

import pandas as pd

data = pd.read_csv('C:/Users/print/Downloads/criminal.csv', encoding='cp949')

data

data.head()

data.info()

data.rename({'서울':'서울특별시'})

data.rename({'서울':'서울특별시'}, axis=1)

data.rename({ 0: '서울특별시'})

data

data.rename({'서울':'서울특별시'}, inplace=True)

data

data.rename({'서울특별시':'서울'}, axis=1)

data

data.rename({'서울특별시':'서울'}, axis=1, inplace=True)

data

data.rename(columns={'서울':'서울특별시'})

data.rename(index={0:'공'})

data.drop('서울')

data.drop('서울', axis=1)

data.drop(columns = '서울')

data.drop(columns = ['서울', '부산'])

data

data['부산']

data.부산

data.경기 고양

data['경기 고양']

data.경기_고양

import seaborn as sns

tips = sns.load_dataset('tips')

tips

tips.sex

tips.sex.value_counts()

mpg = sns.load_dataset('mpg')

mpg

mpg.name.value_counts()

tips.describe()

tips.total_bill

tips[tips.total_bill==3.07]

# map : func + dict
# 한줄만 적용 가능
# series

tips.sex.map({'Female':'F', 'Male':'M'})

tips.sex.map(lambda x : x[0])

tips.sex.map(lambda x : 'F' if x == 'Female' else 'M')

mpg.name

"chevrolet chevelle malibu".split(' ')

mpg.name.map(lambda x : x.split(' ')[0])

mpg.name.map(lambda x : x.split(' ')[0]).value_counts()

'ford' in mpg.name

import numpy as np

np.lookfor('membership')

np.lookfor('contain')

mpg.name.isin

mpg.name.isin(['ford'])

mpg[mpg.name.isin(['ford'])]

mpg.name.isin(['ford']).value_counts()

# duplicated - ML

mpg.duplicated

mpg.duplicated().value_counts()

iris = sns.load_dataset('iris')

iris.duplicated().value_counts()

iris.duplicated(keep=False).value_counts()

iris[iris.duplicated(keep=False)]

iris.drop_duplicates

iris

iris.drop_duplicates()

iris

iris.iloc[:,:-1]

iris.iloc[:,:-1].duplicated(keep=False)

iris[iris.iloc[:,:-1].duplicated(keep=False)]

# type casting
# - type castind : type 변화 문법 없음, 새롭게 만들어야
# - coerce

pd.to_datetime

a = np.array([1,2,3,4])

np.asarray(a)

a.astype('float32')

iris

iris.describe()

iris.boxplot()

tips.describe(include=['category'])

tips.sex.value_counts()

import matplotlib.pyplot as plt

tips.sex.value_counts().plot.bar()

plt.show()

tips.sex.value_counts().plot(kind='pie')

plt.show()

import seaborn as sns

sns.pairplot(iris, hue='species')

plt.show()

tips

tips[tips.sex=='Female'].tip.mean

tips[tips.sex=='Female'].tip.mean()

tips[tips.sex=='Male'].tip.mean()

tips.groupby('sex')['tip'].mean().plot.bar()

plt.show()

plt.ylim([2.5,3])

tips.describe()

tips.tip / tips.total_bill

tips['ratio'] = tips.tip / tips.total_bill

tips

tips.groupby('sex')['ratio'].mean()



a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

np.stack([a,b])

np.concatenate([a,b])

aa = np.array([[1,2,3,4]])
bb = np.array([[10,20,30,40]])

np.stack([aa,bb])

np.concatenate([aa,bb])

np.concatenate([aa,bb], axis=1)

np.stack([aa,bb], axis=1)

np.hstack([aa,bb])

np.vstack([aa,bb])

np.dstack([aa,bb])

np.r_[aa,bb]

np.column_stack((aa,bb))

np.c_[aa,bb]

cc = pd.DataFrame({
    'a' : [1,2,3,4,5]
})

dd = pd.DataFrame({
    'b' : [10,20,30,40,50]
})

cc

dd

pd.concat([cc,dd])

pd.concat([cc,dd], axis=1)

pd.concat([cc,dd], axis=0)

cc = pd.DataFrame({
    'a' : [1,2,3,4,5]
})

dd = pd.DataFrame({
    'a' : [10,20,30,40,50]
})

pd.concat([cc,dd])

pd.concat([cc,dd], ignore_index=True)

aaa = np.arange(24).reshape(6,4)

aaa

np.split(aaa, 2)

aaaa = np.arange(25).reshape(5,5)

aaaa

np.split(aaaa, 2)

np.split(aaa, [1,2])

np.vsplit(aaa, 2)

