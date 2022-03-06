import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
img1 = cv.imread('D:/pics/bai1.jpg',cv.IMREAD_GRAYSCALE)
# img1 = cv.imread('D:/pics/bai1.jpg')
img = cv.resize(img1,(500,500))
sobel = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
# sobel = cv.Sobel(img,cv.CV_16S,1,0,ksize=3)
sobelx = cv.convertScaleAbs(sobel)
# plt.imshow(sobelx1[:,:,::-1])
# plt.show()
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
# sobely = cv.Sobel(img,cv.CV_16S,0,1,ksize=3)
sobely1 = cv.convertScaleAbs(sobely)  #  convertScaleAbs: 可转换可缩放
# plt.imshow(sobely[:,:,::-1])
# plt.show()
sobelxy = cv.addWeighted(sobelx,0.5,sobely1,0.5,0)
# plt.imshow(sobelxy[:,:,::-1])
# plt.show()
cv.imshow('sobelxy',sobelxy)
cv.waitKey(0)
cv.destroyAllWindows()
# plt.imshow(sobelxy[:,:,::-1])
# plt.show()