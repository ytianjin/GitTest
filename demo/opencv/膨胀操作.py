import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/pag2.jpg')
kernel = np.ones((3,3),np.uint8)
pag = cv.erode(img,kernel,iterations=3)
kerne = np.ones((3,3),np.uint8)
pag = cv.dilate(pag,kerne,iterations=3)
plt.imshow(pag[:,:,::-1])
plt.show()