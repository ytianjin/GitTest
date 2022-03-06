import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/img1.jpg')
# 绝对尺寸
# rows,cols = img.shape[:2]
# pag = cv.resize(img,(2*cols,2*rows))
# plt.imshow(pag[:,:,::-1])
# plt.show()
# pag1 = pag.shape
# print(pag1)
# print(rows,cols) 
# 相对尺寸
res = cv.resize(img,None,fx=0.3,fy=0.3)
cv.imwrite('D:/pics/res1.jpg',res)
plt.imshow(res[:,:,::-1])
plt.show()