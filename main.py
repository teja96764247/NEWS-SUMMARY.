from newspaper import Article
import nltk
from textblob import TextBlob
import streamlit as st
import requests
from bs4 import BeautifulSoup


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


    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        related_urls = [a["href"] for a in soup.find_all("a", href=True)]
        st.markdown("<h3 style='font-weight:bold'>Related Articles</h3>", unsafe_allow_html=True)
        for i, related_url in enumerate(related_urls, start=1):
            st.write(f"{i}. {related_url}")
    else:
        st.write("Failed to fetch related articles.")



