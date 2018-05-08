import numpy as np  # a conventional alias
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import nltk
import json
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn import decomposition

file = open("/Users/KrishnChinya/PycharmProjects/Twitter/Tweets.json","r")
json_file = json.loads(file.read())
file.close()

corpus = []
stopwords = ENGLISH_STOP_WORDS

for json in json_file:
    word = json['text']
    # print(word)
    word = word.lower()

    # remove puncuatation and special symbols
    p = string.punctuation
    d = string.digits
    table = str.maketrans(p, len(p) * " ")
    word = word.translate(table)
    table = str.maketrans(d, len(d) * " ")
    word = word.translate(table)
    word = nltk.word_tokenize(word)
    words = [wrd for wrd in word if wrd not in stopwords]
    word = ' '.join(str(wrd) for wrd in words)
    corpus.append(word)

vectorizer = TfidfVectorizer(stop_words = 'english', min_df = 2)
dtm = vectorizer.fit_transform(corpus)

num_topics = 10
num_top_words = 20
clf = decomposition.NMF(n_components = num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)
topic_words = []
for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([corpus[i] for i in word_idx])

for t in range(len(topic_words)):
    print("Topic {}: {}".format(t, ' '.join(topic_words[t][:10])))
