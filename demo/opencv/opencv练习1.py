from ssl import PROTOCOL_TLS
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# img = cv.imread('D:/pics/img.jpg')
img1 = cv.imread('D:/pics/bai1.jpg')
# img2 = cv.addWeighted(img,0.5, img1,0.5,0)
# plt.imshow(img2[:,:,::-1])
# plt.show()
# gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
# pag = cv.GaussianBlur(gray,(35,35),0)
# line = cv.divide(gray,pag, scale=255)
# cv.imshow('line',line)
# cv.waitKey(0)
# cv.destroyAllWindows()
# gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap = plt.cm.gray)
# hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
# plt.imshow(hsv)
# plt.show()
# 绝对尺寸
# rows,cols = img1.shape[:2]
# pag = cv.resize(img1,(1*rows, 2*cols))
# 相对尺寸
pag = cv.resize(img1,None, fx=0.3,fy=0.3)
plt.imshow(pag[:,:,::-1])
plt.show()