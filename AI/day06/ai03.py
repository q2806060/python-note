import nltk.stem.porter as pt 
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb 
import nltk.stem as ns 

words = ['table', 'probably', 'wolves', 'playing', 'is', 'the',
        'beaches', 'grounded', 'dreamt', 'envision']
    
pt_stemmer = pt.PorterStemmer()         # 偏宽松
lc_stemmer = lc.LancasterStemmer()      # 偏严格
sb_stemmer = sb.SnowballStemmer('english')  # 偏中庸
lemmetizer = ns.WordNetLemmatizer()

for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print('%8s %8s %8s %8s' % (word, pt_stem, lc_stem, sb_stem))