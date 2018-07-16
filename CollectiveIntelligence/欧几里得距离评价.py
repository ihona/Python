# coding=utf-8
from CollectiveIntelligence import recommendations
from math import sqrt


def sim_distance(data,person1,person2):
    sim = {}
    for movie in data[person1]:
        if movie in data[person2]:
            sim[movie] = 1
    if len(sim) == 0:
        return 0
    sum_of_squares = sum([pow(data[person1][movie] - data[person2][movie],2) for movie in data[person1] if movie in data[person2]])
    return 1/(1+sqrt(sum_of_squares))

sim_distance(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
