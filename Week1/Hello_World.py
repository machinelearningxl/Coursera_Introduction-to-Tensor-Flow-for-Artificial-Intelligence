# @Author: Antero Maripuu Github:<machinelearningxl>
# @Date : 2019-05-17 12:44
# @Email:  antero.maripuu@gmail.com
# @Project: Coursera
# @Filename : Hello_World.py

import tensorflow as tf
import numpy as np
from tensorflow import keras

#The ‘Hello World’ of neural networks
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')


xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
##