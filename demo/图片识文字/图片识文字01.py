from platform import release
import cv2 as cv
from 文字识别 import img_str

if __name__ == '__main__':

    # 创建窗口
    cv.namedWindow("camera",1)
    # 摄像头 ip摄像头
    video = 'http://...........ip地址'
    capture = cv.VideoCapture(video)
    while True:
        success,img = capture.read()
        cv.imshow("camera",img)
        # 按键
        key = cv.waitKey(10)
        if key == 27:
            #esc
            break
    
        if key == 32:
            # 空格
           filename = 'filename.jpg'
           cv.imwrite(filename,img)
           s = img_str.img_to_str(filename)
           print(s)
    # 释放
    capture.release()
    # 关闭窗口
    cv.destroyWindow("camera")