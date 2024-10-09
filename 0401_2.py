# map : series, function, dict
# applymap, dataframe
# transform : groupby
# apply : series, function
#         dataframe, function
#         applymap
#         axis : 개념 사용

import seaborn as sns

tips = sns.load_dataset('tips')

tips.sex

tips.sex.apply

tips.sex.apply(lambda x: 'F' if x=='Female' else 'M')

tips.select_dtypes('float64')

tips.select_dtypes('float64').apply(lambda x: x+1)

tips.select_dtypes('float64').applymap(lambda x: x+1)

tips

tips.apply(lambda x:x['total_bill'] * x['tip'])

tips.apply(lambda x:x['total_bill'] * x['tip'], axis=1)

tips.apply(lambda x:x['tip'] / x['total_bill'], axis=1)

tips.apply(lambda x:x+1, axis=0)

tips.select_dtypes('float64').apply(lambda x:x+1, axis=0)

tips.select_dtypes('float64').apply(lambda x:sum(x))

dir(tips)

map(lambda x: x+1, [1,2,3,4])

list(map(lambda x: x+1, [1,2,3,4]))

map(lambda x, y: x+y, [1,2,3,4], [3,2,3,4])

list(map(lambda x, y: x+y, [1,2,3,4], [3,2,3,4]))

list(map(lambda x, y: x+y, [1,2,3]))

# facet search



# https://grouplens.org/datasets/movielens/

import pandas as pd

user = pd.read_csv("C:/Users/print/Downloads/users.dat")

user

user = pd.read_csv("C:/Users/print/Downloads/users.dat", sep='::', header=None)

user

user = pd.read_csv("C:/Users/print/Downloads/users.dat", sep='::', header=None, names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])

user

movie = pd.read_csv("C:/Users/print/Downloads/movies.dat", sep = '::', header=None, encoding='latin1')

movie.rename(columns={0:'MovieID', 1:'Title', 2:'Genre'}, inplace=True)

movie

rating = pd.read_csv("C:/Users/print/Downloads/ratings.dat")

rating

user = pd.read_csv("C:/Users/print/Downloads/users.dat", sep='::', header=None, names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'], engine='python')

user

rating = pd.read_csv("C:/Users/print/Downloads/ratings.dat", sep = '::', header=None, encoding='latin1', engine='python')

rating

rating = pd.read_csv("C:/Users/print/Downloads/ratings.dat", sep='::', header=None, engine='python', names=['UserID', 'MovieID', 'Rating', 'Timestamp'])

rating

movie.Genre.map(lambda x : x.split('|'))

movie.Genre.str.split('|') # tuple

movie.Genre.str.split(sep='|')

type(movie.Genre.str.split('|'))

type(movie.Genre.map(lambda x : x.split('|')))

movie.Genre.str.split('|', expand=True)

1 & 3

bin(1)

1 | 3

rating.merge(user)

rating.merge(user).merge(movie)

rating.pivot(index='UserID', columns='MovieID', values='Rating')

tips

tips.pivot('sex', 'smoker', 'tip')

tips.pivot_table('tip', 'sex', 'smoker')

tips.pivot_table('tip', 'sex', 'smoker', margins=True)

tips.pivot_table('tip', ['sex', 'day'], 'smoker', margins=True)

# groupby < margins

pd.crosstab('sex', 'day')

pd.crosstab('sex', 'day', 'size')

pd.crosstab('sex', 'day', 'smoker')

tips.columns

pd.crosstab('sex', ['smoker'])

pd.crosstab('tip', ['smoker'])

import numpy as np

a = np.array(["foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar", "foo","foo", "foo"], dtype=object)
b = np.array(["one", "one", "one", "two", "one", "one", "one", "two", "two", "two", "one"], dtype=object)
c = np.array(["dull", "dull", "shiny" , "dull", "dull", "shiny", "shiny", "dull", "shiny", "shiny", "shiny"], dtype=object)

dd = pd.DataFrame({0:a, 1:b, 2:c})

pd.crosstab(dd.a, dd.b)

pd.crosstab(tips.sex, tips.day)

rating.pivot(index='UserID', columns='MovieID', values='Rating')

rating.drop(columns='Timestamp', inplace=True)

rating

rating.set_index(['UserID', 'MovieID'])

rating.set_index(['UserID', 'MovieID']).unstack()

rating.set_index(['UserID', 'MovieID']).unstack().fillna(0)

de = rating.set_index(['UserID', 'MovieID']).unstack().fillna(0)

de.T

# https://pandas.pydata.org/docs/user_guide/reshaping.html

de1 = de.T.corr() # column-wise, pair-wise

de1

de1[1].nlargest(5)

de1[1].sort_values()

de1[1].sort_values(ascending=False)

de1[1].sort_values(ascending=False)[1:5]

def sim(user_id, n=6):
    return de1[user_id].sort_values(ascending=False)[1:n+1]

sim(3,3)



from sklearn.metrics import pairwise



