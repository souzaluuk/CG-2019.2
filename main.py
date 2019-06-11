import cv2
import numpy as np
from matplotlib import pyplot as plt

def compare_cenario(cenario,placa):
    img1 = placa
    img2 = cenario

    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append([m])

    if (len(good) > 3):
        # img = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
        return True
        # plt.imshow(img),plt.show()
    return False

placas = [ cv2.imread('positivas/placa'+str(x+1)+'.jpg',0) for x in range(14) ]
cenarios = [ cv2.imread('cenarios/cenario'+str(x+1)+'.jpg',0) for x in range(12) ]

resultados = dict()

for i_cenario in range(12):
    nome_cenario = 'cenario'+str(i_cenario+1)+'.jpg'
    resultados[nome_cenario] = []
    for i_placa in range(14):
        if compare_cenario(cenarios[i_cenario], placas[i_placa]):
            nome_placa = 'placa'+str(i_placa+1)+'.jpg'
            print(nome_cenario,':',nome_placa)
            resultados[nome_cenario].append(nome_placa)

print(resultados)
