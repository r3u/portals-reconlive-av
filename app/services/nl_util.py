from nltk import word_tokenize
from nltk.corpus import stopwords
import string

stop = set(stopwords.words('english') + list(string.punctuation))


def tokenize(message: str):
    return [i for i in word_tokenize(message.lower()) if i not in stop]
