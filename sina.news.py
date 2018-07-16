# coding=utf-8
from PIL import Image
import pymysql



def get_Gray(image_file):
    tmpls = []
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            tmpls.append(image_file.getpixel((w, h)))
    return tmpls

# 获取平均灰度值
def get_Avg(ls):
    return sum(ls) / len(ls)

# 比较100个字符有几个字符相同
def get_MH(a, b):
    dist = 0
    for i in range(0, len(a)):
        if a[i] == b[i]:
            dist = dist + 1
    return dist

def get_ImgHash(fne):
    # 打开图片
    image_file = Image.open(fne)
    # 重置图片大小为12px X 12px
    image_file = image_file.resize((12, 12))
    # 转256灰度图
    image_file = image_file.convert("L")
    # 灰度集合
    Gravls = get_Gray(image_file)
    # 灰度平均值
    avg = get_Avg(Gravls)
    # 接收获取0或1
    bitls = ''
    for h in range(1, image_file.size[1] - 1):
        for w in range(1, image_file.size[0] - 1):
            # 像素的值比较平均值，大于记为1，小于记为0
            if image_file.getpixel((w, h)) >= avg:
                bitls = bitls + '1'
            else:
                bitls = bitls + '0'
    return bitls


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




sql = 'select IdentityMale from Cicadellinae大叶蝉 where 序号ID = 4'
img1 = get_ImgHash('D:/4_1.png')
img2 = my_Sql(sql).replace("(('", '').replace("',),)", '')
compare = get_MH(img1, img2)
print(img1)
print(img2)
print(compare)