import cv2
import numpy as np

# 图像元素的访问、通道分离与合并
def salt(img,n):
    for k in range(n):
        i = int(np.random.random()*img.shape[1])
        j = int(np.random.random()*img.shape[0])
        if img.nidm == 2:
            img[j,i] = 255
        elif img.nidm == 3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    return img


img = cv2.imread("D:/test2.jpg")
saltImage = salt(img,500)
cv2.imshow("Salt",saltImage)
cv2.waitKey(0)
cv2.destroyAllWindows()