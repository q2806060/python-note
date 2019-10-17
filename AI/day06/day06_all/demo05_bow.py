"""
demo05_bow.py  词袋模型 bag of word
"""
import sklearn.feature_extraction.text as ft
import nltk.tokenize as tk

doc = 'The brown dog is running. \
	The black dog is in the black room. \
	Running in the room is forbidden.'
# 拆分句子
sents = tk.sent_tokenize(doc)
print(sents)
# 构建词袋模型
model = ft.CountVectorizer()
bow = model.fit_transform(sents)
print(bow.toarray())
print(model.get_feature_names())


