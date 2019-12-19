
"""
-------------------------------编写一个基于UserCF算法的推荐系统-------------------------------

案例描述：
利用ItemCF算法编写一个推荐系统，当用户进行电影浏览时，向用户推荐和该部电影相似的电影。

实现思路：
首先使用训练数据得到用户的偏好信息矩阵和物品的特征信息矩阵，然后计算用户对未进行评分的电影的偏好分，最后选取前K个推荐给用户。
一个基于物品的电影推荐系统实现过程如下：
（1）加载数据集准备数据
（2）使用基于物品的协同过滤算法构建模型
（3）模型训练
（4）效果评估

（1）准备数据
使用MovieLens数据集
（2）选择算法
算法使用的是基于物品的协同过滤算法，电影之间的相似度计算使用的是“优化后的余弦相似度”
（3）模型训练
创建ItemCFRec类：加载评分数据到data、拆分数据集为训练集和测试集、计算物品之间的相似度、为用户进行推荐、进行效果评估

-------------------------------------------------------------摘自《推荐系统开发实战》
"""