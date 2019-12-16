# -*- coding: utf-8 -*-

import random
import math
import os
import json

class ItemCFRec:
    def __init__(self,datafile,ratio):
        # 原始数据路径文件
        self.datafile = datafile
        #测试集与训练集的比例
        self.ratio = ratio

        self.data = self.loadData()
        self.trainData,self.testData = self.splitData(3,47)
        self.items_sim = self.ItemSimilarityBest()

    #加载评分数据到data
    def loadData(self):
        print("加载数据......")
        data = []

    """
        拆分数据集为训练集和测试集
            k:参数
            seed:生成随机数的种子
            M:随机数上限
    """
    def splitData(self,k,seed,M=9):
        pass

    #计算物品之间的相似度
    def ItemSimilarityBest(self):
        pass

    """
        为用户进行推荐
            user:用户
            k:k个临近物品
            nitems:总共返回nitems个物品
    """
    def recommend(self,user,k=8,nitems=40):
        pass

if __name__=="__main__":
    ib = ItemCFRec("../ratings.dat",[1,9])
    print("用户1进行推荐的结果如下：{}".format(ib.recommend("1")))
