import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
import streamlit as st

# Download NLTK resources
nltk.download('punkt')

# Function to scrape related articles from a webpage
def scrape_related_articles(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            related_urls = [a["href"] for a in soup.find_all("a", href=True)]
            return related_urls
        else:
            return []
    except Exception as e:
        print(f"Error scraping related articles: {e}")
        return []

# Function to summarize an article
def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.title, article.authors, article.publish_date, article.summary
    except Exception as e:
        print(f"Error summarizing article: {e}")
        return None, None, None, None

# UI
st.markdown("<h2 style='text-align: center;'>Global Article Summarization and Link Analysis</h2>", unsafe_allow_html=True)

# User input
url = st.text_input("Enter URL:", "")

if url:
    # Summarize the article
    title, authors, publish_date, summary = summarize_article(url)
    if title:
        st.write(f"**Title:** {title}")
        st.write(f"**Authors:** {authors}")
        st.write(f"**Publish Date:** {publish_date}")
        st.write(f"**Summary:** {summary}")
    else:
        st.write("Failed to summarize article.")

    # Fetch related articles
    related_urls = scrape_related_articles(url)
    if related_urls:
        st.markdown("<h3 style='font-weight:bold'>Related Articles</h3>", unsafe_allow_html=True)
        for i, related_url in enumerate(related_urls, start=1):
            st.write(f"{i}. {related_url}")
    else:
        st.write("Failed to fetch related articles.")
