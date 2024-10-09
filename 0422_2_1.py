# https://www.deeplearningbook.org/contents/intro.html



import seaborn as sns

iris = sns.load_dataset('iris')

from sklearn.model_selection import train_test_split

train_test_split(iris)

len(train_test_split(iris))

train, test = train_test_split(iris)

train_test_split(iris.iloc[:,:-1], iris.species)

len(train_test_split(iris.iloc[:,:-1], iris.species))

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.species)

X_train

# data-shift 문제 이런 방식으로 해결 할 수 있음. 랜덤하게 여러번 쪼개서.

y_train

y_train.value_counts()

# stratify

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.species, stratify=iris.species)

y_train.value_counts()

# 데이터가 커도 애매하게 크면 문제 발생 할 수 있으나 이런 방식으로 해결 가능하다.
# 물론 이 방식은 test_size를 결정하면서 문제가 생길 수 있다. over fitting과 under fitting 문제가 발생 가능하다.

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.species, stratify=iris.species, test_size=0.4)

y_train.value_counts()

!pip install mglearn

import mglearn

mglearn.plot_cross_validation.plot_cross_validation()

from sklearn.datasets import load_iris

data = load_iris(as_frame=True)

iris = data.frame

iris

iris.info()

# 차원의 저주

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.target, stratify=iris.target, test_size=0.4)

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

gnb.fit(X_train, y_train)

gnb.predict(X_test) == y_test

sum(gnb.predict(X_test) == y_test)

sum(gnb.predict(X_test) == y_test) / len(y_test)

gnb.score(X_test, y_test)

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.target, stratify=iris.target, test_size=0.4)

gnb.fit(X_train, y_train)

sum(gnb.predict(X_test) == y_test) / len(y_test)

gnb.score(X_test, y_test)

# 할떄마다 달라진다

from sklearn.model_selection import cross_val_score

cross_val_score(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=10)

# overfitting 이라 못 써먹네

cross_val_score(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=5)

# 이정도는 가능할지도

from sklearn.model_selection import learning_curve

learning_curve(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=5)

len(learning_curve(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=5))

learning_curve(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=10)

len(learning_curve(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=10))

train_size, train_score, test_score = learning_curve(GaussianNB(), iris.iloc[:, :-1], iris.target, cv=10)

! pip install -U sklearn-evaluation

import sklearn_evaluation

sklearn_evaluation.plot.learning_curve(train_score, test_score, train_size)

from sklearn.linear_model import LogisticRegression

train_size, train_score, test_score = learning_curve(LogisticRegression(), iris.iloc[:, :-1], iris.target, cv=10)

train_size, train_score, test_score = learning_curve(LogisticRegression(solver='newton-cg'), iris.iloc[:, :-1], iris.target, cv=10)

sklearn_evaluation.plot.learning_curve(train_score, test_score, train_size)

# 복잡도 낮추기 > 뉘앙스를 잃어버림. 모든게 트레이드 오프가 있음



from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(5)

for i in range(2, 21):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    print(i, knn.score(X_test, y_test))



