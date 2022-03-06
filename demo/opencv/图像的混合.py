import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('D:/pics/bai1.jpg')
img3 = cv.imread('D:/pics/fingjin3.jpg')
img2 = cv.resize(img3,(3456,4608))
pag = cv.addWeighted(img2,0.3,img1,0.7,0)
plt.imshow(pag[:,:,::-1])
plt.show()