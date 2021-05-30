import numpy as np
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout
from keras.optimizers import *
from keras.layers.normalization import BatchNormalization
from keras import *
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, Dropout, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import cv2

a = 600
b = 600
model = Sequential()
model.add(Conv2D(50, 5, strides=(2, 2), input_shape=(a, b, 3)))
model.add(MaxPooling2D(5, 5))
model.add(Conv2D(50, 5))
model.add(Dropout(0.018))
model.add(Conv2D(50, 3))
model.add(MaxPooling2D(5, 5))
model.add(Conv2D(50, 3))
model.add(Conv2D(50, 2))
model.add(MaxPooling2D(3, 3))
model.add(Conv2D(50, 2))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dense(1024, activation='relu'))
model.add(Dense(1024, activation='relu'))
model.add(Dense(3))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=adamax(lr=0.001), metrics=['accuracy'])

model.load_weights("Trafik")

def resmiklasordenal(dosyaadi):
    resim = cv2.imread("%s" % dosyaadi)
    return resim

girisverisi = np.array([])
for i in range(90):
    klasordenalinmisresim = 0
    i = i + 1
    print(i)
    string = 'C:/Yuksek Lisans/Proje/Denemeler/Denemeler2/Foto 51/3 sinify/Ornek/%s.png' % i
    klasordenalinmisresim = resmiklasordenal(string)
    girisverisi = np.append(girisverisi, klasordenalinmisresim)

girisverisi = np.reshape(girisverisi, (-1, a, b, 3))
print(model.predict(girisverisi))


