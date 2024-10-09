import seaborn as sns

iris = sns.load_dataset('iris')

iris

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

nb.fit(iris.iloc[:,:-1], iris.species)

nb.predict([[1,3,2,3]])

sns.pairplot(iris, hue='species')



# https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/35179.pdf

# https://www.semanticscholar.org/paper/Scaling-to-Very-Very-Large-Corpora-for-Natural-Banko-Brill/7628b62d64d2e5c33a13a5a473bc41b2391c1ebc



# https://www.kaggle.com/code/karandesaikd/online-food-order-prediction ~~

iris.info()

iris.describe()

iris.boxplot()

iris = iris.iloc[:,:-1]

iris

sns.heatmap(iris, annot = True)



mpg = sns.load_dataset('mpg')

mpg.info()

mpg

mpg.horsepower.isna()

mpg.horsepower.isnull()

mpg[mpg.horsepower.isnull()]

mpg.all()

mpg.isna()

mpg.isna().any()

mpg[mpg.isna().any()]

mpg[mpg.isna().any().columns]

mpg.isna().sum()

mpg.horsepower.isna()

mpg.horsepower.isna().sum()

!pip install -U missingno

import missingno as mimo

dir(mimo)

mimo.bar(mpg)

mimo.matrix(mpg)

# impute



