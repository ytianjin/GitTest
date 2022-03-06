import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/img.jpg')
# plt.imshow(img[:,:,::-1])
# plt.show()
pag = cv.imread('D:/pics/img2.jpg')

img2 = cv.add(img,pag)
plt.imshow(img2[:,:,::-1])
plt.show()
img1 = img + pag
plt.imshow(img1[:,:,::-1])
plt.show()