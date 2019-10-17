"""
demo06_tfidf.py  tfidf转换
"""
import sklearn.feature_extraction.text as ft
import nltk.tokenize as tk
import numpy as np
doc = 'The brown dog is running. \
	The black dog is in the black room. \
	Running in the room is forbidden.'
# 拆分句子
sents = tk.sent_tokenize(doc)
print(sents)
# 构建词袋模型
model = ft.CountVectorizer()
bow = model.fit_transform(sents)
print(model.get_feature_names())

# 通过词袋矩阵  得到tfidf矩阵
tf = ft.TfidfTransformer()
tfidf = tf.fit_transform(bow)
print(np.round(tfidf.toarray(), 2))
