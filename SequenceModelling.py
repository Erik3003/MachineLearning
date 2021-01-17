import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
import numpy as np
import matplotlib.pyplot as plt

class SequenceModelling:

    def __init__(self, units=64, seqlen=10):
        self.SEQLEN = seqlen
        self.UNITS = units

        self.MODEL = Sequential()
        self.MODEL.add(
            SimpleRNN(
                units=self.UNITS,
                return_sequences=False,
                activation="tanh"
            )
        )
        self.MODEL.add(
            Dense(1)
        )
        self.MODEL.compile(optimizer="rmsprop", loss="mean_squared_error")

    def train(self, train_in, train_out, epochs):
        self.MODEL.fit(train_in, train_out, epochs=epochs, verbose=1, validation_split=0.2)

    def predict(self, predict_in):
        return self.MODEL.predict(predict_in)

    def convert_data(self, data):
        data_length = len(data)-self.SEQLEN-1
        input = np.array([[[0.0]]*self.SEQLEN]*data_length)
        output = np.array([[0.0]]*data_length)

        for i in range(data_length):
            output[i, 0] = data[i+self.SEQLEN+1]
            for j in range(self.SEQLEN):
                input[i, j, 0] = data[i+j]

        return [input, output]


if __name__ == '__main__':
    time = np.arange(0, 1000, 0.1)
    sin_wave_train = np.sin(time)
    cos_wave = np.cos(time[:100])

    model = SequenceModelling()
    train_input, train_output = model.convert_data(sin_wave_train)
    test_input, test_output = model.convert_data(cos_wave)

    model.train(train_input, train_output, 10)

    prediction = model.predict(test_input)
    prediction = np.squeeze(prediction)
    test_output = np.squeeze(test_output)
    print(test_output.shape)

    plt.plot(prediction, label="Predicted")
    plt.plot(test_output, label="Real")
    plt.legend()
    plt.show()

