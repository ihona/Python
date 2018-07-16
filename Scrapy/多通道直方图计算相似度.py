# coding=utf-8
# coding=utf-8
import cv2
import pymysql





def my_Sql(statement):
    # 连接数据库
    db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                         charset='utf8')
    # 设置一个游标
    cursor = db.cursor()
    # 执行SQL语句
    cursor.execute(statement)
    # 获得返回结果
    data = cursor.fetchall()
    return str(data)


# 通过得到每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # 将图像resize后，分离为三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree



# db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
#                      charset='utf8')
# cursor = db.cursor()
#
# ima2 = cv2.imread('D:/4_1_TIM.png')
# for i in range(1, 150):
#     sql_img1 = '%s%d' % ('select img1 from Cicadellinae大叶蝉 where 序号ID =', i)
#     cursor.execute(sql_img1)
#     fet = cursor.fetchall()
#     img1 = str(fet).replace("(('", "").replace("',),)", "")
#     if img1 == '0':
#         continue
#     img1_path = 'D:/static/' + img1 + '.png'
#     ima1 = cv2.imread(img1_path)
#     degree1 = classify_hist_with_split(ima1, ima2)
#     print(degree1)\


img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
degree = classify_hist_with_split(img1, img2)

print(degree)