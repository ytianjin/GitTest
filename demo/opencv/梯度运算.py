import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 梯度 = 膨胀 - 腐蚀
img = cv.imread('D:/pics/pag2.jpg')
kernel = np.ones((10,10),np.uint8)
img1 = cv.dilate(img,kernel,iterations=5)
img2 = cv.erode(img,kernel,iterations=5)
# morphologyEx: 形态学. MORPH_GRADIENT: 变形梯度
gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)
plt.imshow(gradient[:,:,::-1])
plt.show()