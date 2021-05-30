import cv2
import numpy as np
import matplotlib.pyplot as plt

def resmiklasordenal(dosyaadi):
    resim = cv2.imread("%s" % dosyaadi)
    return resim

girisverisi = np.array([])
for i in range(255):
    klasordenalinmisresim = 0
    i = i + 1
    string = 'C:/Yuksek Lisans/Proje/Denemeler/Denemeler2/Foto 51/3 sinify/Egitim/%s.png' % i
    klasordenalinmisresim = resmiklasordenal(string)
    girisverisi = np.append(girisverisi, klasordenalinmisresim)
    print(i + 1)

splitverisi=np.array([])
for i in range(90):
    klasordenalinmisresim = 0
    i = i + 1
    string = 'C:/Yuksek Lisans/Proje/Denemeler/Denemeler2/Foto 51/3 sinify/Test/%s.png' % i
    klasordenalinmisresim = resmiklasordenal(string)
    splitverisi = np.append(splitverisi, klasordenalinmisresim)
    print(i + 1)

np.save("girisverimiz", girisverisi)
np.save("splitverimiz", splitverisi)

print(girisverisi.shape)
print(splitverisi.shape)