from re import M
import cv2 as cv
from cv2 import cvtColor
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/wei.jpg', cv.IMREAD_GRAYSCALE)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap = plt.cm.gray)
# plt.show()
v1 = cv.Canny(img,80,150)
v2 = cv.Canny(img,50,100)
res = np.hstack((v1,v2))
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()