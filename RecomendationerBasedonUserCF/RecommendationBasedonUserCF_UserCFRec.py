# -*- coding: utf-8 -*-

import random
import math
import json
import os


class UserCFRec:
    def __init__(self, datafile):
        self.datafile = datafile
        self.data = self.loadData()

        self.trainData, self.testData = self.splitData(3, 47)  #切分训练集和数据集
        self.users_sim = self.UserSimilarityBest()

    #加载评分数据到data
    def loadData(self):
        print("加载数据......")
        data = []
        for line in open(self.datafile):
            userid, itemid, record, _ = line.split("::")
            data.append((userid, itemid, int(record)))
        return data

    """
    拆分数据集为训练集和测试集
      k: 参数
      seed: 生成随机数种子
      M: 随机数上限
    """
    def splitData(self, k, seed, M=8):
        print("训练集与测试集切分......")
        train, test = {}, {}
        random.seed(seed)
        for user, item, record in self.data:
            if random.randint(0, M) == k:
                test.setdefault(user, {})
                test[user][item] = record
            else:
                train.setdefault(user, {})
                train[user][item] = record
        return train, test

    #计算用户之间的相似度，采用惩罚热门商品和优化算法复杂度的算法
    def UserSimilarityBest(self):
        print("开始计算用户之间的相似度......")
        if os.path.exists(
                "datasets/RecomendationerBasedonUserCF-movie/user_sim.json"):
            print("用户相似度从文件加载......")
            userSim = json.load(
                open(
                    "datasets/RecomendationerBasedonUserCF-movie/user_sim.json",
                    "r"))
        else:
            #得到每个item被哪些user评价过
            item_users = dict()
            for u, items in self.trainData.items():
                for i in items.keys():
                    item_users.setdefault(i, set())
                    if self.trainData[u][i] > 0:
                        item_users[i].add(u)
            #构建倒叙表
            count = dict()
            user_item_count = dict()
            for i, users in item_users.items():
                for u in users:
                    user_item_count.setdefault(u, 0)
                    user_item_count[u] += 1
                    count.setdefault(u, {})
                    for v in users:
                        count[u].setdefault(v, 0)
                        if u == v:
                            continue
                        count[u][v] += 1 / math.log(1 + len(users))
            #构建相似度矩阵
            userSim = {}
            for u, related_users in count.items():
                userSim.setdefault(u, {})
                for v, cuv in related_users.items():
                    if u == v:
                        continue
                    userSim[u].setdefault(v, 0.0)
                    userSim[u][v] = cuv / math.sqrt(
                        user_item_count[u] * user_item_count[v])
            json.dump(
                userSim,
                open(
                    "datasets/RecomendationerBasedonUserCF-movie/user_sim.json",
                    "w"))
            return userSim

    """
    为用户user进行物品推荐
      user：为用户user进行物品推荐
      k: 选取k个近邻用户
      nitem: 取nitem个物品
    """
    def recommend(self, user, k=8, nitem=40):
        print("开始为用户user进行物品推荐......")
        result = dict()
        have_score_items = self.trainData.get(user, {})
        for v, wuv in sorted(self.users_sim[user].items(),
                             key=lambda x: x[1],
                             reverse=True)[0:k]:
            for i, rvi in self.trainData[v].items():
                if i in have_score_items:
                    continue
                result.setdefault(i, 0)
                result[i] += wuv * rvi
        return dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True)[0:nitems])


if __name__ == "__main__":
    cf = UserCFRec("datasets\RecomendationerBasedonUserCF-movie/ratings.dat")
    result = cf.recommend("1")
    print("user '1' recommend result is {}".format(result))
