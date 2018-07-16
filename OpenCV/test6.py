# 直方图的计算与显示
import cv2
import numpy as np

img1 = cv2.imread("D:/4_1.png")
img2 = cv2.imread("D:/twb.jpg")
h = np.zeros((256, 256, 3))  # 创建用于绘制直方图的全0图像

bins = np.arange(256).reshape(256, 1)  # 直方图中各bin的顶点位置
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # BGR三种颜色
for ch, col in enumerate(color):
    originHist1 = cv2.calcHist([img1], [ch], None, [256], [0, 256])
    originHist2 = cv2.calcHist([img2], [ch], None, [256], [0, 256])
    cv2.normalize(originHist1, originHist1, 0, 255 * 0.9, cv2.NORM_MINMAX)
    cv2.normalize(originHist2, originHist2, 0, 255 * 0.9, cv2.NORM_MINMAX)
    hist1 = np.int32(np.around(originHist1))
    hist2 = np.int32(np.around(originHist2))
    pts1 = np.column_stack((bins, hist1))
    pts2 = np.column_stack((bins, hist2))
    cv2.polylines(h, [pts1], False, col)
    h1 = np.flipud(h)
    cv2.polylines(h, [pts2], False, col)
    h2 = np.flipud(h)




cv2.imshow("colorhist1", h1)
cv2.imshow("colorhist2", h2)
cv2.waitKey(0)