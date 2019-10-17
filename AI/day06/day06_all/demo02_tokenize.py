"""
demo02_tokenize.py  分词器
"""
import nltk.tokenize as tk
doc = "Are you curious about tokenization? \
	Let's see how it works! \
	We neek to analyze a couple of sentences \
	with punctuations to see it in action."
# print(doc)

sent_list = tk.sent_tokenize(doc)
for i, sent in enumerate(sent_list):
	print('%2d' % (i+1), sent) 

word_list = tk.word_tokenize(doc)
for i, word in enumerate(word_list):
	print('%2d' % (i+1), word) 

tokenizer = tk.WordPunctTokenizer()
word_list = tokenizer.tokenize(doc)
for i, word in enumerate(word_list):
	print('%2d' % (i+1), word) 




