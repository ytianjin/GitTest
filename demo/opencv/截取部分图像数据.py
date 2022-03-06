import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/bai1.jpg')
pag = img[100:500,0:200]       # 利用切片的方法
plt.imshow(pag[:,:,::-1])
plt.show()