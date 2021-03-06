import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    pairs = len(series)-window_size
    
    for i in range(pairs):
        X.append(series[i:window_size+i])
        
    y = series[window_size:]

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    
    rnn = Sequential()
    rnn.add(LSTM(5, input_shape=(window_size,1)))
    rnn.add(Dense(1))
    return rnn

    
    


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    azlist = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for c, value in enumerate(list(set(text))):
        if (value not in azlist and value not in punctuation):
            text = text.replace(value," ");
            

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    for i in range(0, len(text)-window_size,step_size):
        inputs.append(text[i:window_size+i])
        
    outputs = [a for a in text[window_size::step_size]]
    
    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    rnn = Sequential()
    rnn.add(LSTM(200, input_shape=(window_size,num_chars)))
    rnn.add(Dense(num_chars, activation = 'softmax'))
    return rnn
