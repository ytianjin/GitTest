import cv2 as cv


def get_iamge_info(iamge):
    print(type(iamge))
    print(iamge.shape)
    print(iamge.size)
    print(iamge.dtype)


src = cv.imread("D:/pics/input image.jpg")
cv.namedWindow('src', cv.WINDOW_AUTOSIZE)
cv.imshow("src", src)
get_iamge_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2BGRA)
cv.imwrite("D:/result1.png", gray)
cv.waitKey(0) 

cv.destroyAllWindows()