from newspaper import Article
import nltk
from textblob import TextBlob
import streamlit as st

st.markdown("<h2 style='text-align: center;'>NEWS SUMMARY</h2>", unsafe_allow_html=True)

nltk.download('punkt')



url = st.text_input("Enter URL:")

if url:
    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    main_image_url=article.top_image
    st.image(main_image_url)

    
    st.markdown("<h3 style='font-weight:bold'>Tittle Of the Article</h3>", unsafe_allow_html=True)
    st.write(article.title)



    st.markdown("<h3 style='font-weight:bold'>Authors Of the Article</h3>", unsafe_allow_html=True)
    st.write(article.authors)



    st.markdown("<h3 style='font-weight:bold'>Publish Date Of the Article</h3>", unsafe_allow_html=True)
    st.write(article.publish_date)


    st.markdown("<h3 style='font-weight:bold'>Summary Of the Article</h3>", unsafe_allow_html=True)
    st.write(article.summary)



