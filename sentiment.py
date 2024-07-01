import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')


# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Function to preprocess text (e.g., remove stopwords)
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

# Streamlit app layout
def main():
    st.title('Sentiment Analysis App')
    st.sidebar.title('Menu')
    text = st.text_area('Enter text to analyze:')
    preprocess = st.checkbox('Preprocess text')

    if st.button('Analyze'):
        if text:
            if preprocess:
                text = preprocess_text(text)
            sentiment = analyze_sentiment(text)
            st.write(f'Sentiment: {sentiment}')

if __name__ == '__main__':
    main()
