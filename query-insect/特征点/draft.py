# coding=utf-8
import cv2

img = cv2.imread('D:/zsb.jpg')
img2 = cv2.imread('D:/hwp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
kp = surf.detect(gray, None)
kp2 = surf.detect(gray2, None)

img = cv2.drawKeypoints(gray, kp, img)
img2 = cv2.drawKeypoints(gray2, kp2, img2)

cv2.imshow("img", img)
cv2.imshow('img2', img2)

k = cv2.waitKey(0)
if k & 0xff == 27:
    cv2.destroyAllWindows()