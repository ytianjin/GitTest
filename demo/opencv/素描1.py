import cv2 as cv
import numpy

img = cv.imread('D:/pics/2.jpg')
img = cv.resize(img,(500,500))
cv.imshow('img', img)
gloi = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
line = cv.GaussianBlur(gloi, (75, 75), 0)
a = cv.divide(gloi, line, scale=255)  # divide = 分开，分散 scale = 规模
cv.imshow('a', a)
cv.waitKey(0)
# cv.waitKey(0)
# cv.destroyAllWindows()