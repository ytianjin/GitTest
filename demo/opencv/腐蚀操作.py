import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/pag2.jpg')
kerne = np.ones((5,5),np.uint8)         # iterations = 次数;迭代;迭代次数
pag = cv.erode(img,kerne,iterations = 3) # erode = 侵蚀;腐蚀
plt.imshow(pag[:,:,::-1])
plt.show()
