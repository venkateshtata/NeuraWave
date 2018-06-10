#importing libraries
from keras.preprocessing import sequence
from keras.layers import Dense
import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, SimpleRNN
import matplotlib.pyplot as plt

max_features = 10000  # number of words to consider as features
maxlen = 100  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

#loading the data
print('Loading data...')
input_train = np.load("X_train.npy")
y_train = np.load("Y_train.npy")
input_test = np.load("X_test.npy")
y_test = np.load("Y_test.npy")



#printing the sequences
print(len(input_train), 'train sequences')
print(len(input_test), 'test sequences')

#training and testing data
print('Pad sequences (samples x time)')
input_train = sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = sequence.pad_sequences(input_test, maxlen=maxlen)

print('input_train shape:', input_train.shape)
print('input_test shape:', input_test.shape)
print(input_train.shape[0])
print(input_train.shape[1])



input_train = np.reshape(input_train, (input_train.shape[0], input_train.shape[1], input_train.shape[2]))
input_test = np.reshape(input_test, (input_test.shape[0], input_test.shape[1], input_test.shape[2]))

#lstm
from keras.layers import LSTM

model = Sequential()
#model.add(Embedding(max_features, 32))
model.add(LSTM(128, return_sequences = True, input_shape = (input_train.shape[1], 5)))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128, return_sequences = True))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics = ['acc'])
model.fit(input_train, y_train,
                    epochs=100,
                    batch_size=128,
                    validation_split=0.2)

model.predict(input_test)


