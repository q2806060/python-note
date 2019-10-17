"""
demo07_news.py  主题识别
读取20news文件夹, 每个文件夹的文件夹名
作为类别标签, 文件夹中的没有文件作为样本, 
构建tfidf矩阵, 交给朴素贝叶斯模型训练.   

自定义测试样本, 测试每句话的主题属于哪一类别.
"""
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import numpy as np

train = sd.load_files('../ml_data/20news', 
	encoding='latin1', shuffle=True, 
	random_state=7)

# train.data: 返回每个文件的字符串内容
# train.target: 返回每个文件的父目录名(类别名)
print(np.array(train.data).shape)
print(np.array(train.target).shape)

# 整理输入集 输出集
train_data = train.data
train_y = train.target
categories = train.target_names # 类别名
cv = ft.CountVectorizer()
bow = cv.fit_transform(train_data)
tf = ft.TfidfTransformer()
train_x = tf.fit_transform(bow)
# 选择使用朴素贝叶斯 进行模型训练
model = nb.MultinomialNB()
model.fit(train_x, train_y)

# 测试集  测试模型是否可用
test_data = [
	'The curveballs of right handed pitchers \
	tend to curve to the left.', 
	'Caesar cipher is an ancient form of \
	encryption.',
	'This two-wheeler is really good on slippery \
	roads.']

bow = cv.transform(test_data)
tfidf = tf.transform(bow)
pred_y = model.predict(tfidf)

for sent, index in zip(test_data, pred_y):
	print(sent, '->', categories[index])







