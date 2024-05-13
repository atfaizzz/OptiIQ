import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
def pre_process(text):
    stop_words = set(stopwords.words('english'))
    new_words = ["fig", "figure", "image", "sample", "using",
                 "show", "result", "large",
                 "also", "one", "two", "three",
                 "four", "five", "seven", "eight", "nine"]
    stop_words = list(stop_words.union(new_words))

    text = text.lower()
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)
    text = re.sub("(\\d|\\W)+", " ", text)
    text = text.split()
    text = [word for word in text if word not in stop_words]
    text = [word for word in text if len(word) >= 3]
    lmtzr = WordNetLemmatizer()
    text = [lmtzr.lemmatize(word) for word in text]

    return ' '.join(text)
