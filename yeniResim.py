import cv2
import numpy as np
import matplotlib.pyplot as plt


def resmiklasordenal(dosyaadi):
    resim = cv2.imread("%s" % dosyaadi)
    resim = cv2.resize(resim, (600, 600))
    mask = np.zeros_like(resim)
    cv2.fillConvexPoly(mask, np.array([[0, 515], [125, 370], [200, 370], [45, 600],[0, 600]]), (255, 255, 255))
    resim = cv2.bitwise_and(resim, mask)
    return resim

for i in range(462):
    klasordenalinmisresim = 0
    i = i + 1
    print(i)
    string = 'C:/Yuksek Lisans/Proje/Denemeler/Denemeler2/Foto 51/numaralandirma/%s.png' % i
    klasordenalinmisresim = resmiklasordenal(string)
    cv2.imwrite('C:/Yuksek Lisans/Proje/Denemeler/Denemeler2/Foto 51/maskeli/%s.png' % i, klasordenalinmisresim)

