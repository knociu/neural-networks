import numpy as np
import matplotlib.pyplot as plt

def fourier_transform(x):
    a = np.abs(np.fft.fft(x))
    a[0] = 0
    return a/np.amax(a)

class Adaline(object):
    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=100):
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = np.random.random(2 * self.no_of_inputs + 1) - 0.5
        self.errors = []

    def train(self, training_data_x, training_data_y, name):
        #training_data_x = self._standarize(training_data_x)

        #normalize data
        training_data_x = self._normalize(training_data_x)
        training_data_y = self._normalize(training_data_y)
      
        training_data_x = [i * 0.8 + 0.1 for i in training_data_x]
        training_data_y = [j * 0.8 + 0.1 for j in training_data_y]


        #random data
        np.random.shuffle(training_data_x)
        np.random.shuffle(training_data_y)


        for _ in range(self.iterations):
            e = 0
            for x, y in zip(training_data_x, training_data_y):
                x = np.concatenate([x, fourier_transform(x)])
                out = self.output(x)
                self.weights[1:] += self.learning_rate * (y - out) * x * out * (1 - out)
                self.weights[0] += self.learning_rate * (y - out) * out * (1 - out)
                e += (y - out)**2
            self.errors.append(e)
        plt.plot(range(len(self.errors)), self.errors)
        plt.savefig('learning_curve_' + str(name) + '.pdf')
        plt.close()

    def _standarize(self, training_data_x):
        return ((training_data_x - np.mean(training_data_x)) / np.std(training_data_x))

    def _normalize(self, training_data_x):
        return (training_data_x - np.min(training_data_x)) / (np.max(training_data_x) - np.min(training_data_x))

    def _activation(self, x):
        return 1/(1 + np.exp(-x))

    def _activation_derivative(self, x):
        return 1

    def output(self, input):
        return self._activation(np.dot(self.weights[1:], input) + self.weights[0])

    def predict(self, input):
        input = self._normalize(input)
        x = np.concatenate([input, fourier_transform(input)])
        return self._activation(np.dot(self.weights[1:], x) + self.weights[0])