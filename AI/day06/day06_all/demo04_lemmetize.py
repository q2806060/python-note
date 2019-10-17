"""
demo04_lemmetize.py  词性还原
"""
import nltk.stem as ns

words = ['table', 'probably', 'wolves', 
	'playing', 'is', 'the', 'beaches', 
	'grouded', 'dreamt', 'envision']

lemmatizer = ns.WordNetLemmatizer()
for word in words:
	n_lemm = lemmatizer.lemmatize(word,pos='n')
	v_lemm = lemmatizer.lemmatize(word,pos='v')
	print('%8s %8s %8s' % \
		  (word, n_lemm, v_lemm))