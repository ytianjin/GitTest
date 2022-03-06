import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('D:/pics/img1.jpg')
rows,cols = img1.shape[:2]
m = np.float32([[1,0,100],[0,1,50]])
res = cv.warpAffine(img1,m,(cols,rows))
plt.imshow(res[:,:,::-1])
plt.show()