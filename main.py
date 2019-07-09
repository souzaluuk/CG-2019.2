import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import utils

def compare_cenario(cenario,placa):
    img1 = placa
    img2 = cenario

    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    good = []
    set_matches = dict()
    for m,n in matches:
        if m.distance/n.distance < 0.8:
            set_matches[m.trainIdx] = m

    if len(set_matches) > 1:
        keysNoOutliers = utils.noOutliers(list(set_matches.keys()))
        good = [ [set_matches[key]] for key in keysNoOutliers]

    if (len(good) > 5):
        # img = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
        # plt.imshow(img),plt.show()
        return True
    return False

lista_placas = os.listdir('positivas')
lista_cenarios = os.listdir('cenarios')

placas = [ cv2.imread('positivas/'+placa,0) for placa in lista_placas ]
cenarios = [ cv2.imread('cenarios/'+cenario,0) for cenario in lista_cenarios ]

resultados = dict()

for i_cenario in range(len(lista_cenarios)):
    nome_cenario = lista_cenarios[i_cenario]
    resultados[nome_cenario] = []
    for i_placa in range(len(lista_placas)):
        e1 = cv2.getTickCount()
        if compare_cenario(cenarios[i_cenario], placas[i_placa]):
            nome_placa = lista_placas[i_placa]
            print(nome_cenario,':',nome_placa,end=' ')
            resultados[nome_cenario].append(nome_placa)
        e2 = cv2.getTickCount()
        time = (e2 - e1)/cv2.getTickFrequency()
        print('tempo:',str(time)+'s')

print()
for cenario in resultados.keys():
    print(cenario,':',resultados[cenario])
