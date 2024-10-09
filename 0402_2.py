rating = pd.read_csv("C:/Users/print/Downloads/ratings.dat", sep='::', header=None, engine='python', names=['UserID', 'MovieID', 'Rating', 'Timestamp'])

rating

rating.drop(columns='Timestamp', inplace=True)

de = rating.set_index(['UserID', 'MovieID']).unstack().fillna(0)

de.T

de1 = de.T.corr()

de1

pd.to_pickle(de1, 'reco')

dd = pd.read_pickle('reco')

dd





import seaborn as sns

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

# groupby < margins

rating.drop(columns='Timestamp', inplace=True)

rating

rating.set_index(['UserID', 'MovieID'])

rating.set_index(['UserID', 'MovieID']).unstack()

rating.set_index(['UserID', 'MovieID']).unstack().fillna(0)

de = rating.set_index(['UserID', 'MovieID']).unstack().fillna(0)

de.T



data = pd.read_pickle('reco')

data

data[1]

data.iloc[1]

data.loc[1]

data.loc[1].sort_values()

data.loc[1].sort_values(ascending=False)

data.loc[1].sort_values(ascending=False)[1:6]

tips = sns.load_dataset('tips')

tips

tips.index

tips.columns

tips.columns

tips.values

tips.set_index('sex')

tips.set_index('sex').sort_index()

tips.set_index('sex').sort_index().loc['Male']



de1 = pd.read_pickle('reco')

de1

de1[1].nlargest(5)

de1[1].sort_values()

de1[1].sort_values(ascending=False)

de1[1].sort_values(ascending=False)[1:5]

def sim(user_id, n=6):
    return de1[user_id].sort_values(ascending=False)[1:n+1]

sim(3,3)

sim(3,3).index

rating[rating.UserID==3000]

rating[(rating.UserID==3000)|(rating.UserID==479)|(rating.UserID==5691)]

# a==3 or a==6
# a in [3,6]

(rating.UserID.isin([3000,479]))

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1]
    return rating.UserID.isin(index)

sim_movie(3,3)

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    return rating[rating.UserID.isin(index)]

sim_movie(3,3)

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    return rating[rating.UserID.isin(index)]['MovieID'].values

sim_movie(3,3)

len(set(sim_movie(3,3)))

rating[rating.MovieID==661]

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    return rating[(rating.UserID.isin(index))&(rating.Rating==5)]

sim_movie(3)

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    return rating[(rating.UserID.isin(index))&(rating.Rating==5)]['MovieID']

sim_movie(3)

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    return rating[(rating.UserID.isin(index))&(rating.Rating==5)][['MovieID']]

sim_movie(3)

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    return rating[(rating.UserID.isin(index))&(rating.Rating==5)]['MovieID'].values

sim_movie(3)

import numpy as np

np.unique([1,2,1,2,1,1,])

np.unique([1,2,1,2,1,1,], return_counts=True)

np.histogram([1,2,1,2,1,1,], bins=2)

tips.sex.unique()

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    movie = rating[(rating.UserID.isin(index))&(rating.Rating==5)]['MovieID'].values
    return np.unique(movie)

sim_movie(3)

movie.MovieID.isin(sim_movie(3))

movie[movie.MovieID.isin(sim_movie(3))]

def sim_movie(user_id, n=6):
    index = de1[user_id].sort_values(ascending=False)[1:n+1].index
    movie_ = rating[(rating.UserID.isin(index))&(rating.Rating==5)]['MovieID'].values
    movieid = np.unique(movie_)
    return movie[movie.MovieID.isin(movieid)]

sim_movie(3)



# https://www.jstor.org/stable/1578601?seq=1

# intrinsically linear

# https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf



