import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# imgg = cv.imread('D:/pics/img.jpg')
img = cv.imread('D:/pics/res1.jpg')
# # hsv = cv.cvtColor(imgg,cv.COLOR_BGR2HSV) 
# # plt.imshow(hsv)
# # pag = cv.add(imgg,img)
# pag = imgg + img
# plt.imshow(pag)
# plt.show()
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
pag = cv.GaussianBlur(gray,(75,75),0)
line = cv.divide(gray, pag, scale=255)
cv.imshow('line', line)
cv.waitKey()
cv.destroyAllWindows()
# plt.imshow(gray,cmap = plt.cm.gray)