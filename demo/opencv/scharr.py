
import numpy as np
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('D:/pics/bai1.jpg',0)
img = cv.resize(img1,(500,500))
scharr = cv.Scharr(img,cv.CV_64F,0,1)
scharry = cv.Scharr(img,cv.CV_64F,1,0)
scharrx = cv.convertScaleAbs(scharr)
scharry1 = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx,0.5,scharry1,0.5,0)
cv.imshow('scharrxy',scharrxy)
cv.waitKey(0)
cv.destroyAllWindows()                                                                                                           
