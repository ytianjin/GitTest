import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建图像
img = np.zeros((512,512,3),np.uint8)
# 绘制图形
cv.line(img,(0,0),(511,511),(255,0,0),5) 
# 第一个括号表示直线的起点,第二个表示终点,第三个表示线条的颜色,5表示线条的宽度
cv.circle(img,(256,256),60,(0,0,255),4)
cv.rectangle(img,(100,100),(400,400),(0,255,0),5)
cv.putText(img,"hello",(100,150),cv.FONT_HERSHEY_COMPLEX,5,(255,255,255),3)
# 显示效果
plt.imshow(img[:,:,::-1])
plt.show()