import cv2 as cv
import matplotlib.pyplot as plt

# cv.IMREAD_COLOR  以彩色模式加载图像,用(1)代表
# cv.IMREAD_GRAYSCALE 以灰度模式加载图像,用(0)代表
# cv.IMREAD_UNCHANGED 以alpha通道加载图像,用(-1 )代表
src = cv.imread('D:/pics/input image.jpg', 0)
# cv.imshow('gre', src)
# cv.waitKey(0)
# cv.destroyAllWindows()
# plt.imshow(src[:,:,::-1])
plt.imshow(src, cmap=plt.cm.gray)  # 这是以灰色通道展示图像
plt.show()