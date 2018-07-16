# coding=utf-8
from math import sqrt

def readfile(filename):
    lines = [line for line in open(filename)]

    #第一行是标题
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # 每行的第一列是行名
        rownames.append(p[0])
        # 剩余部分就是该行对应的数据
        data.append([float(x) for x in p[1:]])
    return rownames, colnames, data

# 皮尔逊相关度
def pearson(v1, v2):
    # 简单求和
    sum1 = sum(v1)
    sum2 = sum(v2)

    # 求平方和
    sum1Sq = sum([pow(v, 2) for v in v1])
    sum2Sq = sum([pow(v, 2) for v in v2])

    # 求乘积之和
    pSum = sum([v1[i] * v2[i] for i in range(len(v1))])

    # 计算r (Pearson score)
    num = pSum-(sum1*sum2/len(v1))
    den = sqrt((sum1Sq-pow(sum1, 2)/len(v1))*(sum2Sq-pow(sum2, 2)/len(v1)))
    if den == 0:
        return 0
    return 1.0-num/den


class bicluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.distance = distance
        self.id = id


def hcluster(rows, distance = pearson):
    distance={}
    currentcluster = -1

    # 最开始的聚类就是数据中的行
    clust = [bicluster(rows[i], id=1) for i in range(len(rows))]




















