import cv2 as cv
src = cv.imread(r'D:/pics/input image.jpg')
gray = cv.cvtColor(src, cv.IMREAD_GRAYSCALE)
cv.imshow('imge', src)
cv.imshow('src', gray)
# cv.imwrite('D:/result1.png', src, [int(cv.IMWRITE_PNG_COMPRESSION), 0 ])
# cv.imwrite('D:/result2.png', src, [int(cv.IMWRITE_PNG_COMPRESSION), 9 ])
cv.imwrite('D:/result1.jpg', src, [int(cv.IMWRITE_JPEG_QUALITY), 5])
cv.imwrite('D:/result2.jpg', src, [int(cv.IMWRITE_JPEG_QUALITY), 100])
cv.waitKey(0)

cv.destroyAllWindows()