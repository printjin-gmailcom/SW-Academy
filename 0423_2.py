import seaborn as sns

from sklearn.datasets import load_wine, load_breast_cancer

data = load_wine(as_frame=True)

wine = data.frame

wine.info()

sns.pairplot(wine, hue='target')

wine.boxplot(figsize=(10,4))

from sklearn.pipeline import Pipeline

pipe = Pipeline()

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

pipe = Pipeline([('std', StandardScaler()), ('knn', KNeighborsClassifier())])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(wine.iloc[:,:-1], wine.target)

pipe.fit(X_train, y_train)

from sklearn import set_config

set_config(display='diagram')

pipe.predict(X_test)

pipe.score(X_test, y_test)

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

knn.score(X_test, y_test)

from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(KNeighborsClassifier(), param_grid={'n_neighbors':[5,6,7]})

grid.fit(X_train, y_train)

import pandas as pd

pd.DataFrame(grid.cv_results_).T

# grid2 = GridSearchCV(pi\a)

pipe2 = Pipeline([('pre',StandardScaler()),('clf',KNeighborsClassifier())])

pipe2.get_params()

from sklearn.preprocessing import MinMaxScaler

from sklearn.linear_model import LogisticRegression

grid2 = GridSearchCV(pipe2, [{'clf': [KNeighborsClassifier(), LogisticRegression()]},
                             {'clf__n_neighbors':[5,6,7], 'pre':[MinMaxScaler(), StandardScaler()]}])

grid2.fit(X_train, y_train)

pd.DataFrame(grid2.cv_results_).T



# 분석 (맹신하지 말고 참고)
# 복잡한 모델일수록 오버피팅 많이 생김 - 데이터 많이 필요
# 복잡한 모델이 성능이 좋음

# 데이터 수집 ( 어렵다 )
# 간단한 모델 선택 > 작은 데이터 (컬럼)

# filter
# wrapper
# embeded



wine = data.frame

wine.info()

wine



from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()

dt.fit(X_train, y_train)

from sklearn.tree import plot_tree

plot_tree(dt)

dt.feature_importances_



wine.corr()

wine.boxplot(figsize=(11,6))

sns.heatmap(wine.corr())

from sklearn.feature_selection import SelectKBest, chi2

skb = SelectKBest(chi2, k=7)

skb

skb.fit_transform(X_train, y_train)

vars(skb)

dir(skb)

skb.get_feature_names_out()

# 13c7

from sklearn.feature_selection import RFE

from sklearn.linear_model import LogisticRegression

rfe = RFE(LogisticRegression(), n_features_to_select=7)

rfe

rfe.fit_transform(X_train, y_train)

vars(rfe)

from sklearn.decomposition import PCA

import mglearn

mglearn.plot_pca.plot_pca_illustration()

pca = PCA(7)

pca.fit_transform(X_train, y_train)

# OvsAll(Rest) / Ovso

# LogisticRegression

from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier

ov = OneVsRestClassifier(LogisticRegression())



# Ensemble



