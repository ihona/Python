# coding=utf-8
import cv2
import numpy as np
def salt(img, n):
# 从k=0到k=n，默认以步长1
  for k in range(n):
    # 产生随机数（0~1）*图像的宽
    i = int(np.random.random()* img.shape[1]);
    # 产生随机数（0~1）*图像的高
    j = int(np.random.random() *img.shape[0]);
    # 如果图像是二维的
    if img.ndim == 2:
      img[j,i] = 255
    # 如果图像是三维的
    elif img.ndim == 3:
      # 分别给三个通道的对应像素点赋值
      img[j,i,0]= 255
      img[j,i,1]= 255
      img[j,i,2]= 255
  return img
if __name__ == '__main__':
  img = cv2.imread("图像路径")
  saltImage = salt(img, 500)
  cv2.imshow("Salt", saltImage)
  cv2.waitKey(0)
  cv2.destroyAllWindows()