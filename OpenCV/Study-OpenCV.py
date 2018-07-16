import cv2
img = cv2.imread("D:/test1.jpg")
print(img.shape)
# (628,941,3)
print(img.size)
# 1772844
print(img.dtype)
# uint8