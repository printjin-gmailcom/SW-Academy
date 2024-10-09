from sklearn.datasets import load_iris

data = load_iris(as_frame=True)

iris = data.frame

iris

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier((64,64))

mlp.fit(iris.iloc[:, :-1], iris.target)



import tensorflow as tf

# https://www.coursera.org/specializations/tensorflow-advanced-techniques?action=enroll

model = tf.keras.Sequential()

model.add(tf.keras.layer.Dense(64), input_shape=(4,))

model.add(tf.keras.layer.Dense(64))

model.add(tf.keras.layer.Dense(3))

model.summary()



model2 = tf.keras.Sequential([
    tf.keras.layer.Dense(64), input_shape=(4,)
    tf.keras.layer.Dense(64)
    tf.keras.layer.Dense(3)
])

model2.summary()



model3 = tf.keras.Sequential([
    tf.keras.layer.Dense(64), input_shape=(4,)
    tf.keras.ReLU()
    tf.keras.layer.Dense(64)
    tf.keras.layer.Dense(3)
])



model4 = tf.keras.Sequential([
    tf.keras.layer.Dense(64), input_shape=(4,)
    tf.keras.ReLU()
    tf.keras.layer.Dense(64, activation='relu')
    tf.keras.layer.Dense(3)
])



model5 = tf.keras.Sequential([
    tf.keras.layer.Dense(64), input_shape=(4,)
    tf.keras.ReLU()
    tf.keras.Activation('relu')
    tf.keras.layer.Dense(3)
])



# https://keras.io/guides/



# model.compile()

# compile == cimputation graph 형식으로 변환하겠다. 효율적으로 학습시켜줌. 아니면 직접 학습 코드 짜서 해야함.



model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy)

model.compile(loss='sparse_categorical_crossentropy') # 옵션을 못 넣음

model.compile(loss=tf.keras.losses.sparse_categorical_crossentropy) # high other function 형태 활용



model.fit(iris.iloc[:,:-1], iris.target)

model.fit(iris.iloc[:,:-1], iris.target, epochs=10)

# 이떄 loss 값이 감소하는 상태가 아니면 함수가 잘못 된 것으로 판단



model = tf.keras.Sequential([
    tf.keras.layer.Dense(64), input_shape=(4,)
    tf.keras.ReLU()
    tf.keras.Activation('relu')
    tf.keras.layers.Activation('softmax')
    tf.keras.layer.Dense(3)
])

model.fit(iris.iloc[:,:-1], iris.target, epochs=10)



