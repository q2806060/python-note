"""
demo08_movie_reviews.py 电影推荐
"""
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
import numpy as np

# 存储正面数据
pdata = []
# 读取语料库中movie_reviews文件夹中的pos文件夹
# 把每个文件的文件名返回
fileids = nc.movie_reviews.fileids('pos')
# 遍历每个文件, 把文件信息存入pdata
for fileid in fileids:
	sample = {}
	# 对全文进行分词  得到words列表
	words = nc.movie_reviews.words(fileid)
	for word in words:
		sample[word] = True
	pdata.append((sample, 'POSITIVE'))

# 存储负面数据
ndata = []
# 读取语料库中movie_reviews文件夹中的neg文件夹
# 把每个文件的文件名返回
fileids = nc.movie_reviews.fileids('neg')
# 遍历每个文件, 把文件信息存入pdata
for fileid in fileids:
	sample = {}
	# 对全文进行分词  得到words列表
	words = nc.movie_reviews.words(fileid)
	for word in words:
		sample[word] = True
	ndata.append((sample, 'NEGATIVE'))

# 拆分测试集与训练集 (80% 训练集)
pnumb, nnumb = \
	int(len(pdata)*0.8), int(len(ndata)*0.8)
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
print(np.array(train_data).shape)
print(np.array(test_data).shape)

# 基于朴素贝叶斯模型, 训练测试数据
model=cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)

# 模拟业务场景
reviews = [
 'It is an amazing movie. ',
 'This is a dull movie, I would never \
  recommend it to anyone. ', 
 'The cinematography is pretty great \
  in this movie. ', 
 'The direction was terrible and the story \
  was all over the place. ']

for review in reviews: 
	sample = {}
	words = review.split() # 野蛮分词
	for word in words:
		sample[word] = True
	# classify类似predict方法, 通过样本预测类别
	pred_y = model.classify(sample)
	print(review, '->', pred_y)
