import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def text_preprocessing(text):
    #text = input("Enter the text :")
    text = re.sub(r'[^a-z\s]', '', str(text).lower().strip())
    text = word_tokenize(text)
    stop_words = stopwords.words('english')
    stop = ['u','us']
    stop_words = stop_words + stop
    text = [word for word in text if word not in stop_words]
    word_lem = WordNetLemmatizer()
    news_text = [word_lem.lemmatize(word,pos='v') for word in text]
    return news_text

