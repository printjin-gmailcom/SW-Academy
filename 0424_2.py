from sklearn.datasets import load_iris

data = load_iris(as_frame =True)

iris = data.frame

iris

from sklearn.model_selection import cross_val_score

cross_val_score(LogisticRegression(), iris.iloc[:,:-1], iris.target, cv=10)

from sklearn.linear_model import LogisticRegression

cross_val_score(LogisticRegression(), iris.iloc[:,:-1], iris.target, cv=10)

from sklearn.neighbors import KNeighborsClassifier

cross_val_score(KNeighborsClassifier(), iris.iloc[:,:-1], iris.target, cv=10)

from sklearn.model_selection import cross_val_predict

cross_val_predict(KNeighborsClassifier(), iris.iloc[:,:-1], iris.target, cv=10)

from sklearn.model_selection import KFold

cv = KFold()

cv.split(iris.iloc[:,:-1], iris.target)

t = cv.split(iris.iloc[:,:-1], iris.target)

next(t)

from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold()

cv.split(iris.iloc[:,:-1], iris.target)

t = cv.split(iris.iloc[:,:-1], iris.target)

next(t)

cross_val_predict(KNeighborsClassifier(), iris.iloc[:,:-1], iris.target, cv=cv)



# model = algorithm + data

from sklearn.ensemble import VotingClassifier

import joblib

vc = VotingClassifier([('knn', KNeighborsClassifier()), ('Ir', LogisticRegression())])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.iloc[:,:-1], iris.target)

vc.fit(X_train, y_train)

vars(vc)

dir(vc)

from sklearn.ensemble import BaggingClassifier

bb =  BaggingClassifier()

bb.fit(X_train, y_train)

bb =  BaggingClassifier(LogisticRegression())

bb.fit(X_train, y_train)

from sklearn.ensemble import StackingClassifier

StackingClassifier

Ir = LogisticRegression()

Ir.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, Ir.predict(X_test))



