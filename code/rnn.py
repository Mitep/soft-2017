import numpy as np
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Activation
from keras.utils import np_utils
from scipy import misc
from PIL import Image
import os

def build_model(input_length=1024, output_length=3):
    model = Sequential()
    
    #input layer
    model.add(LSTM(20, input_shape=(None, 1024), return_sequences=True))
    model.add(Dropout(0.2))
    #hidden layer/layers
    model.add(LSTM(40, return_sequences=True))
    model.add(Dropout(0.2))
    #output layer
    model.add(Dense(output_length))
    model.add(Activation('linear'))

    model.compile(loss='mse', optimizer='rmsprop')
    return model

def train_rnn(model, wav_path, midi_path):
    start_time = time.time()
    print('Train started on ' + str(start_time))
    X_data = misc.imread(os.path.join(wav_path, 'input.png'))
    Y_data = misc.imread(os.path.join(midi_path, 'output.png'))
    X_data = np.rot90(X_data, 3)
    Y_data = np.rot90(Y_data, 3)
    X_data = X_data.reshape(1, 70320, 1024)
    Y_data = Y_data.reshape(1, 70320, 3)
    model.fit(X_data, Y_data, batch_size=40, nb_epoch=5, verbose=1)
    finish_time = time.time()
    print('Train finished on ' + str(finish_time))
    return model
