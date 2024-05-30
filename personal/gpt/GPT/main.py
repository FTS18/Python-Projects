import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Function to load and preprocess data from text file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data.lower()

# Function to create training data
def create_training_data(text, max_sequence_len):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    total_words = len(tokenizer.word_index) + 1

    input_sequences = []
    for line in text.split('\n'):
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]

    return predictors, label, total_words, max_sequence_len

# Function to define and train the model
def create_model(predictors, label, total_words, max_sequence_len):
    model = Sequential()
    model.add(Embedding(total_words, 10, input_length=max_sequence_len-1))
    model.add(LSTM(150, return_sequences = True))
    model.add(LSTM(150))
    model.add(Dense(total_words, activation='softmax'))

    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(predictors, label, epochs=100, verbose=1)
    
    return model

# Function to generate text based on user input
def generate_text(seed_text, next_words, max_sequence_len, model, tokenizer):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Main function
def main():
    file_path = 'text.txt'
    text = load_data(file_path)
    predictors, label, total_words, max_sequence_len = create_training_data(text, max_sequence_len=20)
    model = create_model(predictors, label, total_words, max_sequence_len)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'train':
            corrected_output = input("Correct output: ")
            corrected_output = corrected_output.lower()
            text += '\n' + corrected_output
            predictors, label, total_words, max_sequence_len = create_training_data(text, max_sequence_len=20)
            model = create_model(predictors, label, total_words, max_sequence_len)
            tokenizer = Tokenizer()
            tokenizer.fit_on_texts([text])
            print("Model retrained successfully!")
        else:
            response = generate_text(user_input, 10, max_sequence_len, model, tokenizer)
            print("Bot:", response)

if __name__ == "__main__":
    main()
