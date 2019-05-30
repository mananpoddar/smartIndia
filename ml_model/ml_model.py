from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler as ss
import numpy as np
from sklearn.model_selection import train_test_split
import pickle

input_dim = 11

def get_model():
    model = Sequential()
    model.add(Dense(32, input_dim = input_dim))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dense(8))
    model.add(Activation('relu'))
    model.add(Dense(2))
    model.add(Activation('softmax'))
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return model

def get_data(tt_split = 0.8):
    not_fraud = pd.read_csv('../data/data.csv', header = 'infer')
    not_fraud['is_fraud'] = 0
    not_fraud['is_not_fraud'] = 1
    fraud = pd.read_csv('../data/data_fraud.csv', header = 'infer')
    fraud['is_fraud'] = 1
    fraud['is_not_fraud'] = 0
    res =  shuffle(pd.concat([fraud, not_fraud]))
    res['slum'] = 0
    res['middle'] = 0
    res['posh'] = 0
    res.loc[res.area == 'slum', 'slum'] = 1
    res.loc[res.area == 'middle', 'middle'] = 1
    res.loc[res.area == 'posh', 'posh'] = 1
    x = res[['lower_education','higher_education','jewellery','car','bike','tax','misc_credit','misc_debit','slum','middle','posh']]
    scaler = ss().fit(x)
    x = scaler.transform(x)
    y = res[['is_fraud','is_not_fraud']]
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=tt_split, random_state=42)
    return (x_train, x_test, y_train, y_test, scaler)

def main():
    model = get_model()
    x_train, x_test, y_train, y_test, scaler = get_data()
    model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data = (x_test, y_test))
    model.save('data.h5')
    with open('scaler', 'wb') as fscaler:
        pickle.dump(scaler, fscaler)

main()