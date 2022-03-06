import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# img = np.zeros((256,256,3),np.uint8)
img = cv.imread('D:/pics/img.jpg')
cv.imread('D:/pics/img1.jpg')

# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows() 
# plt.imshow(img[:,:,::-1])
# plt.imshow(img, cmap = plt.cm.gray)
# img[100,100] = (0,0,255)
# # plt.imshow(img[:,:,::-1])
# print(img.shape)
# print(img.dtype)
# print(img.size)
# b,g,r = cv.split(img)
# plt.imshow(b,cmap = plt.cm.gray)
# img2 = cv.merge((b,g,r))
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# plt.imshow(gray,cmap = plt.cm.gray)
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# plt.imshow(hsv)
# plt.show()