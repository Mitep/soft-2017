import numpy as np
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
from keras.utils import np_utils

def build_model(input_lenght, output_length):
    model = Sequential()
    
    #input layer
    model.add(LSTM(20, input_shape=(input_lenght,), return_sequences=True))
    model.add(Dropout(0.2))

    #hidden layer/layers
    model.add(LSTM(40, return_sequences=True))
    model.add(Dropout(0.2))

    #output layer
    model.add(Dense(output_length))
    model.add(Activation('linear'))

    model.compile(loss='mse', optimizer='rmsprop')
    
    return model

def train_rnn(model, data, epochs=10):
    train_start_time = time.time()

    X_train, y_train = data

    model.fit(X_train, y_train, batch_size=512, nb_epoch=epochs, verbose=1, validation_split=0.05)

    train_end_time = time.time()

    return model, train_start_time, train_end_time

def predict(input):
    '''
    ucitaj model
    '''
    return input