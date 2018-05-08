import pandas as pd
import json
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import nltk

file = open("/Users/KrishnChinya/PycharmProjects/Twitter/data.json","r")
json_file = json.loads(file.read())
file.close()

states_abbrevation = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


tweets = pd.DataFrame(columns=["States","Text"]);
columns = list(tweets)

length_json = len(json_file)
pos = 1
words = []
state = ""
stopwords = ENGLISH_STOP_WORDS
for json in json_file:
    word = json['text']
    # print(word)
    word = word.lower()
    # word = word.decode("utf-8")

    #remove puncuatation and special symbols
    p = string.punctuation
    d = string.digits
    table = str.maketrans(p, len(p)*" ")
    word = word.translate(table)
    table = str.maketrans(d, len(d)*" ")
    word = word.translate(table)

    word = nltk.word_tokenize(word)
    # print(word)

    words = [wrd for wrd in word if wrd not in stopwords]
    # print(words)

    if(json['place']!=None):
        state = json['place']['full_name'].split(',')[1].strip()
        if state not in states_abbrevation.keys():
            for key,value in states_abbrevation.items():
                if value.lower() == json['place']['full_name'].split(',')[0].lower():
                    state = key
                    break;
                state = 'unknown'
        else:
            for key, value in states_abbrevation.items():
                if key == state:
                    state = key
                    break;
    else:
        state = 'unknown'

    if(pos < length_json):
        if(tweets.size != 0):
            if((tweets['States'] == state).any()):
                tweets['Text'].values[0].extend(words)
                # tweets.append(words)
            else:
                tweets.loc[tweets.size] = [state, words];
        else:
            tweets.loc[tweets.size] = [state, words];

sentiment = {};

# here calculating scores
file = open("/Users/KrishnChinya/PycharmProjects/Twitter/AFINN-111.txt")
for f in file.readlines():
    lst = f.split()
    if(len(lst) == 2):
        name = lst[0]
        scores = lst[1]
    else:
        name = "";
        while(len(lst)>=2):
            if(len(name) == 0):
                name = lst[0]
                lst.remove(name)
            else:
                name = name + " " +lst[0]
                lst.remove(lst[0])
            if(len(lst) == 1):
                scores = lst[0]
    sentiment[name] = int(scores)
file.close()

state_scores = pd.DataFrame(columns=["States","Score"]);

sentiment_score = 0;
for index, row in tweets.iterrows():
    for key, value in sentiment.items():
        for tweet_word in row[1]:
            if(tweet_word == key):
                sentiment_score = sentiment_score + int(value)
    state_scores.loc[state_scores.size] = [row[0], sentiment_score]
    sentiment_score = 0

state_scores.to_csv("/Users/KrishnChinya/PycharmProjects/Twitter/scores1.csv",index=False)