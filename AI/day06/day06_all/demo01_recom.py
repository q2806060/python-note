"""
demo01_recom.py  推荐引擎
"""
import json
import numpy as np
'''
1. 读取json文件, 遍历每一个用户, 计算当前
   用户与其他用户的相似度(欧式距离得分)
2. 把每个相似度得分,存入scmat矩阵.供以后使用
'''
with open('../ml_data/ratings.json', 'r')as f:
	ratings = json.loads(f.read())

users, scmat = list(ratings.keys()), []
for user1 in users:
	scrow = [] # 存储user1与其他人的相似度得分
	for user2 in users:
		movies = set()
		# user1看过的user2也看过
		for movie in ratings[user1]:
			if movie in ratings[user2]:
				movies.add(movie)
		# 两人没有共同语言
		if len(movies) == 0:
			score = 0
		else:  # 两人有都看过的电影
			x, y = [], []
			for movie in movies:
				x.append(ratings[user1][movie])
				y.append(ratings[user2][movie])
			x = np.array(x)
			y = np.array(y)
			#score = 1/(1+np.sqrt(((x-y)**2).sum()))
			score = np.corrcoef(x,y)[0,1]
		scrow.append(score)
	scmat.append(scrow)

users = np.array(users)
scmat = np.array(scmat)
# 输出每个用户的相关系数得分矩阵
for scrow in scmat:
	print('  '.join(
	'{:.2f}'.format(score) for score in scrow))

# 按照相关系数从高到低排列每个用户的相似度
for i, user in enumerate(users):
	sorted_indices = scmat[i].argsort()[::-1]
	# 忽视当前user
	sorted_indices = \
		sorted_indices[sorted_indices!=i]
	# 获取相似用户数组
	similar_users = users[sorted_indices]
	# 获取每个相似用户的相似度得分
	similar_scores = scmat[i, sorted_indices]
	#print(user, similar_users, similar_scores,
	#	sep='\n')

	# 生成推荐清单
	# 找到所有正相关用户即相关性分数
	positive_mask=similar_scores > 0
	similar_users=similar_users[positive_mask]
	similar_scores=similar_scores[positive_mask]
	# 存储对当前用户的推荐的电影
	# recomm_movies = {'电影名':[0.5, 0.4, 0.3]}
	recomm_movies = {}
	for i, similar_user in \
				enumerate(similar_users):
		# 拿到相似用户看过, 但user没看过的电影
		for movie, score in \
				ratings[similar_user].items():
			if movie not in ratings[user].keys():
				if movie not in recomm_movies:
					recomm_movies[movie]=[score]
				else:
					recomm_movies[movie].append(score)

	print(user)
	#print(recomm_movies)
	movie_list = sorted(recomm_movies.items(), 
		key=lambda x:np.average(x[1]), 
		reverse=True)
	print(movie_list)






