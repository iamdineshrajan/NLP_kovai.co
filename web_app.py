import pickle
from preprocessing import text_preprocessing
from gensim import corpora,models
import streamlit as st
from PIL import Image
dictionary_model = pickle.load(open('C:/Users/DELL/NLP/dictionary.pkl','rb'))
loaded_model = pickle.load(open('C:/Users/DELL/NLP/model.pkl','rb'))

def categorize(text):
    var = ''
    dtm = dictionary_model.doc2bow(text_preprocessing(text))
    dtm_score = sorted(loaded_model[dtm],key = lambda x: -1*x[1])[0][1]
    if dtm_score >= 0.2:
        var = "Category number:" + str(sorted(loaded_model[dtm],key = lambda x: -1*x[1])[0][0]+1)
    else:
            var = 'Not in this category'
    if text == '':
        var = 'News is missing,Please enter the news'
    return var

def main():
    
    st.title('The US Stock Market News')
    news = st.text_area('Enter the News')
    
    if st.button('Categorize'):
        categorize(news)
    result = categorize(news)
    if result == "Category number:1":
        cat1 = Image.open('C:/Users/DELL/NLP/Category1.png')
        st.image(cat1)
    elif result == "Category number:2":
        cat2 = Image.open('C:/Users/DELL/NLP/Category2.png')
        st.image(cat2)
    elif result == "Category number:3":
        cat3 = Image.open('C:/Users/DELL/NLP/Category3.png')
        st.image(cat3)
    st.success(result)

if __name__ == '__main__':
    main()