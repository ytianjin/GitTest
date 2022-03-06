import cv2 as cv
from cv2 import imshow

img = cv.imread('D:/pics/2.jpg', 0)
img = cv.resize(img,(500,500))
gray = cv.GaussianBlur(img,(5, 5),0)
# blur = cv.divide(img,gray, scale=255)
# cv.threshold(gray)
can = cv.Canny(gray, 30, 70)
# 寻找轮廓
contours, hierarchy = cv.findContours(can, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
cv.drawContours(img, contours, -1, (0, 0, 255), 1)
imshow('blur', img)
cv.waitKey()