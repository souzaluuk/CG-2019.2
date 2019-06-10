import cv2
import numpy as np
import matplotlib.pyplot as plt
# import objects as obj

img1 = cv2.imread('placas/r24a.jpg', 0)
img2 = cv2.imread('cenarios/cenario7.jpg', 0)
# img2 = cv2.equalizeHist(img2)

# objs = obj.get_objects(img2)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good = []
for m,n in matches:
  if m.distance < 0.75 * n.distance:
    good.append([m])

img = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

plt.imshow(img),plt.show()