# coding=utf-8
import cv2

img = cv2.imread('D:/lena.jpg')
cv2.namedWindow('img',0)
cv2.moveWindow('img',50,600)
cv2.resizeWindow('img',600,200)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()