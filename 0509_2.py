# -*- coding: utf-8 -*-
"""0509_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Sr8kW_2v8708o_3nZczvdye6o2UGtbx7
"""

# tensorflow downgrade

import tensorflow as tf

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
])

model.summary()

model.weights



