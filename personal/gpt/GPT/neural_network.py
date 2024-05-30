import numpy as np
import pickle

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward_pass(self, X):
        # Input to hidden layer
        self.hidden_output = self.sigmoid(np.dot(X, self.weights_input_hidden) + self.bias_input_hidden)
        # Hidden to output layer
        self.output = self.sigmoid(np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_hidden_output)
        return self.output

    def train(self, X, y, epochs=1000, learning_rate=0.1):
        for epoch in range(epochs):
            # Forward pass
            output = self.forward_pass(X)

            # Backpropagation
            error = y - output
            output_delta = error * self.sigmoid_derivative(output)
            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)

            # Update weights and biases
            self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
            self.bias_hidden_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
            self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
            self.bias_input_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def save_model(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_model(filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)
