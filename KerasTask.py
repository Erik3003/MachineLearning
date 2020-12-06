import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data(path='mnist.npz')

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(layers.Flatten(input_shape=(28,28,1)))
model.add(layers.Dense(45))
model.add(layers.Dense(10))

opt = keras.optimizers.Adam(learning_rate=0.7)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=10)
model.evaluate()
