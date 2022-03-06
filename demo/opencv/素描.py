import cv2 as cv
import numpy

img = cv.imread('D:/pics/input image.jpg', 1)
cv.imshow('img', img)
height = img.shape[0]
width = img.shape[1]
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
dat = 255 - gray
data_gauss = cv.GaussianBlur(dat, (9, 9), 0)
a = cv.divide(dat, data_gauss, scale=255)
cv.imshow('a', a)
cv.imwrite('D:/pics/paint.jpg', a)
cv.waitKey(0)