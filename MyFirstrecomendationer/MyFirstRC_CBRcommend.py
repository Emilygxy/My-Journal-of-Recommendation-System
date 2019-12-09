import json
import pandas as import pd
import numpy as np
import math
import random

class CBRecommend:
    # 加载dataProcessing.py中处理的数据
    def __init__(self,K):
        pass
    
    #获取用户未进行评分的item列表
    def get_none_score_item(self,user):
        pass

    #获取用户对item的喜好程度
    def cosUI(self,user,item):
        pass

    #为用户进行电影推荐
    def recommend(self,user):
        pass

if __name__=="__main__":
    cb=CBRecommend(K=10)
    cb.recommend()

