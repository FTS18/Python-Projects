import numpy as np
from neural_network import NeuralNetwork

class Chatbot:
    def __init__(self, model_filepath, text_data_filepath):
        self.language_model = NeuralNetwork.load_model(model_filepath)
        self.text_data = self.load_text_data(text_data_filepath)

    def load_text_data(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            text_data = file.read().split()
        return text_data

    def text_to_vector(self, text):
        # Convert text input into a vector using one-hot encoding
        vector = np.zeros(len(self.text_data))
        for word in text.split():
            if word in self.text_data:
                vector[self.text_data.index(word)] = 1
        return vector.reshape(1, -1)  # Reshape the vector to have shape (1, num_features)

    def generate_response(self, input_text):
        input_vector = self.text_to_vector(input_text)
        output = self.language_model.forward_pass(input_vector)
        # Assuming binary classification, round to get predicted class
        predicted_class = round(output[0][0])
        if predicted_class == 1:
            return "I'm sorry, I didn't understand that."
        else:
            # Implement response generation based on input text
            if "movie" in input_text.lower():
                return "What's your favorite movie?"
            else:
                return "I'm sorry, I don't know how to respond to that."
