# coding=utf-8
import cv2

img = cv2.imread("D:/zsb.jpg")
# print(img)
r,b,g = cv2.split(img)
cv2.imshow('Red',r)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.waitKey(0)
cv2.destroyAllWindows()