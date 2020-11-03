import numpy as np
import random as rn

class Perceptron:
    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=100):
        self.iterations = iterations
        self.no_of_inputs = no_of_inputs
        self.learning_rate = learning_rate
        self.weights = np.random.random(self.no_of_inputs + 1) - 0.5

    def train(self, training_data, labels):
        life_span, best_life_span = 0, 0
        a, record = 0, 0
        pocket = self.weights

        for _ in range(self.iterations):
            #get random example
            i = rn.randrange(len(training_data))

            #calculate prediction
            prediction = self.predict(training_data[i])

            #check
            if labels[i] - prediction == 0:
                life_span += 1
                
                #check all training_data
                for input, label in zip(training_data, labels):
                    if label - self.predict(input):
                        a += 1
                
                if a > record and life_span > best_life_span:
                    record = a
                    best_life_span = life_span
                    pocket = self.weights
            else:
                self.weights[1:] += self.learning_rate * (labels[i] - prediction) * training_data[i]
                self.weights[0] += self.learning_rate * (labels[i] - prediction)
                life_span = 0
                a = 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0