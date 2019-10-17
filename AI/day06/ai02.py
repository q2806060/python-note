import nltk.tokenize as tk 


doc = "Are you curious about tokenization? Let's see how it work! \
        We neek to analyze a couple of sentences with punctuations to see it in action."
# print(doc)

sent_list = tk.sent_tokenize(doc)

for i, sent in enumerate(sent_list):
    print('%2d' % (i+1), sent) 

tk.word_tokenize('')