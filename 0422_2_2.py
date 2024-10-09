from sklearn.datasets import load_wine

data = load_wine(as_frame=True)

wine = data.frame

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(wine.iloc[:, :-1], wine.target)

from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(KNeighborsClassifier(), {'n_neighbors': range(2,21), 'algorithm':['ball_tree', 'brute'], 'weights':['uniform', 'distance']}, cv=5)

grid.fit(X_train, y_train)

grid.best_estimator_

grid.best_index_

grid.best_params_

grid.best_score_

grid.cv_results_

import pandas as pd

pd.DataFrame(grid.cv_results_).T



!pip install numpy scipy scikit-learn pandas joblib pytorch

! pip install deap update_checker tqdm stopit xgboost

! pip install tpot

import tpot

from tpot import TPOTClassifier



# https://scholar.google.co.kr/scholar?q=james+bergstra+yoshua+bengio&hl=ko&as_sdt=0&as_vis=1&oi=scholart

# orange



