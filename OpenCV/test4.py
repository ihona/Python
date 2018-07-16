# 分离、合并通道
import cv2
import numpy as np

img = cv2.imread("D:/test2.jpg")
b,g,r = cv2.split(img)
# 其中split返回RGB三个通道，如果只想返回其中一个通道，可以这样：
# b = cv2.split(img)[0]
# g = cv2.split(img)[1]
# r = cv2.split(img)[2]
cv2.imshow("Blue",r)
cv2.imshow("Red",g)
cv2.imshow("Green",b)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 也可以直接操作NumPy数组来达到这一目的：
# import cv2
# import numpy as np
#
# img = cv2.imread("D:/cat.jpg")
#
# b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
# g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
# r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
#
# b[:, :] = img[:, :, 0]
# g[:, :] = img[:, :, 1]
# r[:, :] = img[:, :, 2]
#
# cv2.imshow("Blue", r)
# cv2.imshow("Red", g)
# cv2.imshow("Green", b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

