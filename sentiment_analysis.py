import time
import tweepy
import streamlit as st
import joblib
import re
import numpy as np
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

# Twitter API Credentials (Replace with your actual keys)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJuTzwEAAAAAKE1Gb56GbfCHwj%2FFFWSS5RR5QD0%3DLxEBx4vpOpJUTc8wm24OwOuC5hfO0lkPDX7dy4VCkP2PJR5MQk"

# Initialize Tweepy Client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Load Trained Sentiment Analysis Model
MODEL_PATH = "sentiment_analysis.sav"  # Ensure this file is in the same directory
VECTORIZER_PATH = "tfidf_vectorizer.sav"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Function to clean tweets
def clean_tweet(tweet):
    """Preprocess tweet text: remove mentions, hashtags, links, and special characters."""
    tweet = re.sub(r"@\w+|#\w+|http\S+", "", tweet)  # Remove mentions, hashtags, URLs
    tweet = re.sub(r"[^a-zA-Z\s]", "", tweet)  # Keep only alphabets
    return tweet.strip().lower()

# Function to predict sentiment
def predict_sentiment(text):
    """Predict sentiment using trained ML model."""
    cleaned_text = clean_tweet(text)
    text_vector = vectorizer.transform([cleaned_text])
    prediction = model.predict(text_vector)
    return "Positive" if prediction == 1 else "Negative"

# Function to fetch tweets
def fetch_tweets(query, count=10):
    """Fetch tweets while handling rate limits."""
    try:
        response = client.search_recent_tweets(
            query=query, max_results=count, tweet_fields=["text"]
        )

        if response.data:
            return [tweet.text for tweet in response.data]
        return []

    except tweepy.TooManyRequests:
        st.warning("Rate limit exceeded. Retrying after 60 seconds...")
        time.sleep(60)
        return fetch_tweets(query, count)

    except tweepy.TweepyException as e:
        st.error(f"Error fetching tweets: {e}")
        return []

# Streamlit App
st.title("Twitter Sentiment Analysis")

query = st.text_input("Enter a keyword or hashtag:")
tweet_count = st.slider("Number of tweets to fetch:", min_value=1, max_value=20, value=5)

if st.button("Analyze Sentiment"):
    tweets = fetch_tweets(query, tweet_count)
    
    if tweets:
        st.write("Fetched Tweets and Sentiment Analysis:")
        for tweet in tweets:
            sentiment = predict_sentiment(tweet)
            st.write(f"- **Tweet:** {tweet}\n  **Sentiment:** {sentiment}")
    else:
        st.write("No tweets found.")
