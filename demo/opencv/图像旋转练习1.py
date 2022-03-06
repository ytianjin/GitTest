import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('D:/pics/bai1.jpg')
img3 = cv.imread('D:/pics/fingjin3.jpg')
img2 = cv.resize(img3,(3456,4608))
img1_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img1_gray,10,255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
new_img2 = cv.bitwise_and(img1,img1, mask=mask_inv)
line = cv.addWeighted(img1,0.3, new_img2,0.7,0)
plt.imshow(line[:,:,::-1])
plt.show() 