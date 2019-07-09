import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import utils

sift = cv2.xfeatures2d.SIFT_create()

lista_placas = sorted(os.listdir('positivas'))[:1] # [:1] seleciona as imagens (neste caso uma apenas)
print(lista_placas)
placas = [ cv2.imread('positivas/'+placa,0) for placa in lista_placas ]

placas = [ [img]+list(sift.detectAndCompute(img, None)) for img in placas]

def compare_cenario(cenario,placa):
    img1, kp1, des1 = placa

    img2 = cenario
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
        img = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
        # plt.imshow(img),plt.show()
        return (True,img)
    return (False,None)

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    for placa in placas:
        valid, new_frame = compare_cenario(frame,placa)
        if valid:
            frame = new_frame

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()