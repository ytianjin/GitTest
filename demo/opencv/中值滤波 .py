import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/bai1.jpg')
median = cv.medianBlur(img,5)
plt.imshow(median[:,:,::-1])
plt.show()