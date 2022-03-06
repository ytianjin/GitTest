import cv2
# 轮廓检测
img = cv2.imread('D:/pics/2.jpg')
img = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 获取灰度图
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)  # 利用阈值自动选择的方法获取二值图像
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 检测轮廓
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)  # 画出轮廓
cv2.imshow('gray', binary)
cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

