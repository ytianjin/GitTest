import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/bai1.jpg')
rows,clos,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,398]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
m = cv.getPerspectiveTransform(pts1,pts2)
line = cv.warpPerspective(img,m,(1000,1000))
plt.imshow(line[:,:,::-1])
plt.show() 