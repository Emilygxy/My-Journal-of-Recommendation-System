import pandas as pd
import json


class DataProcessing:
    def __init__(self):
        pass

    def process(self):
        print("开始转换用户数据(users.dat)...")
        self.process_user_data()
        print("开始转换电影数据(movies.dat)...")
        self.process_movies_data()
        print("开始转换用户对电影评分数据(ratings.dat)...")
        self.process_rating_data()
        print('Over!')

    def process_user_data(self, file="datasets/users.dat"):
        fp = pd.read_table(
            file,
            sep='::',
            engine='python',
            names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
        fp.to_csv('datasets/users.csv', index=False)

    def process_rating_data(self, file="datasets/ratings.dat"):
        fp = pd.read_table(file,
                           sep='::',
                           engine='python',
                           names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
        fp.to_csv('datasets/ratings.csv', index=False)

    def process_movies_data(self, file="datasets/movies.dat"):
        fp = pd.read_table(file,
                           sep='::',
                           engine='python',
                           names=['MovieID', 'Title', 'Genres'])
        fp.to_csv('datasets/movies.csv', index=False)


if __name__ == '__main__':
    dp = DataProcessing()
    dp.process()