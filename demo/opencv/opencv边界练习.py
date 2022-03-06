import cv2 as cv
from cv2 import IMREAD_GRAYSCALE
from cv2 import Canny
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/wei.jpg')
pag = cv.resize(img,None, fx=0.3,fy=0.3)
gray = cv.cvtColor(pag,cv.COLOR_BGR2GRAY)
pts1 = cv.Canny(gray,80,100)
pts2 = cv.Canny(gray,20,100)
resp = np.hstack((pts1,pts2))
cv.imshow('resp',resp)
cv.waitKey(0)
cv.destroyAllWindows()
# plt.imshow(resp[:,:,::-1])
# plt.show()