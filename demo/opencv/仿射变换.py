import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/pics/pag1.jpg')
rows,clos = img.shape[:2]
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[100,100],[200,50],[100,250]])
m = cv.getAffineTransform(pts1,pts2)
png = cv.warpAffine(img,m,(clos,rows))
plt.imshow(png[:,:,::-1])
plt.show()