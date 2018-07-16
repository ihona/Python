# 输出文本
import cv2
image=cv2.imread('D:/test1.jpg')
cv2.putText(image, 'Hello World', (300,100), 0, 0.5, (0,0,255),0)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()