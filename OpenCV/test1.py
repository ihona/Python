import cv2
# 获取图像
img = cv2.imread("D:/test2.jpg")
# 创建一个窗口
cv2.namedWindow("Image")
# 在窗口中显示图像
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 创建/复制图像
import numpy as np
# 新的OpenCV的接口中没有CreateImage接口。即没有cv2.CreateImage这样的函数。
# 如果要创建图像，需要使用numpy的函数（现在使用OpenCV-Python绑定，numpy是必装的）
emptyImage = np.zeros(img.shape,np.uint8)
# 在新的OpenCV-Python绑定中，图像使用NumPy数组的属性来表示图像的尺寸和通道信息。
# 如果输出img.shape，将得到(500, 375, 3)，这里是以OpenCV自带的cat.jpg为示例。
# 最后的3表示这是一个RGB图像
# 复制原有的图像来获得一副新图像
emptyImage2 = img.copy()
# 还可以用cvtColor获得原图像的副本
emptyImage3 = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
# 将其转成空白的黑色图像
#emptyImage3[...]=0

# 保存图像
# 第一个参数是保存的路径及文件名，第二个是图像矩阵。其中，imwrite()有个可选的第三个参数，如下：
# cv2.imwrite("D:\\cat2.jpg", img，[int(cv2.IMWRITE_JPEG_QUALITY), 5])
# 第三个参数针对特定的格式： 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95
# cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int
# 对于PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，从0到9,压缩级别越高，图像尺寸越小。默认级别为3
cv2.imwrite("D:/test2-1.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),5])
cv2.imwrite("D:/test2-2.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
cv2.imwrite("D:/test2-3.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
cv2.imwrite("D:/test2-4.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])
cv2.waitKey(0)
cv2.destroyAllWindows()