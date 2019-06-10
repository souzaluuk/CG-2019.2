import cv2
import numpy as np
from matplotlib import pyplot as plt

def compare_cenario(cenario):
    img1 = cv2.imread(cenario,0)

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
        img = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
        plt.imshow(img),plt.show()

img2 = cv2.imread('cenarios/cenario9.jpg',0)
for i in range(14):
    compare_cenario('placas1/placa'+str(i+1)+'.jpg')