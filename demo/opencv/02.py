import cv2 as cv

img = cv.imread('D:/pics/2.jpg')
up = cv.pyrUp(img)
down = cv.pyrDown(up)
cv.imshow('up', up)
cv.waitKey()
