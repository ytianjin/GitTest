import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/pag1.jpg')
# 2 图像旋转
rows,clos = img.shape[:2]
# 2.1 生成旋转矩阵
m = cv.getRotationMatrix2D((clos/2,rows/2),90,1)
# 2.2 进行旋转变换
pag = cv.warpAffine(img,m,(rows,clos))
plt.imshow(pag[:,:,::-1])
plt.show()