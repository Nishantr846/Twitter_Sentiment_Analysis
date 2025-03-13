# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 15:14:14 2025

@author: Nishant
"""

import streamlit as st
import tweepy
import pandas as pd
import os
from dotenv import load_dotenv
from textblob import TextBlob

# Load environment variables
load_dotenv()

# Twitter API credentials (loaded from .env file)
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

if not BEARER_TOKEN:
    st.error("Error: BEARER_TOKEN not found! Check your .env file.")
    st.stop()

# Authenticate with Twitter API v2
try:
    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)
    print("Successfully authenticated with Twitter API.")
except Exception as e:
    print(f"Authentication failed: {e}")


# Define sentiment labels
def get_sentiment(text):
    """Analyzes sentiment using TextBlob."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def fetch_tweets(query, count=10):
    """Fetches tweets using Twitter API v2."""
    try:
        response = client.search_recent_tweets(query=query, max_results=count, tweet_fields=["text"])
        if response.data:
            return [tweet.text for tweet in response.data]
        else:
            return []
    except tweepy.TweepyException as e:
        st.error(f"Error fetching tweets from Twitter API: {e}")
        return []

# Streamlit UI
st.title("Twitter Sentiment Analysis")
st.write("Enter a topic to fetch recent tweets and analyze sentiment.")

# User input
query = st.text_input("Enter a topic or keyword", "Twitter")
tweet_count = st.slider("Number of tweets to fetch", min_value=5, max_value=50, value=10)

if st.button("Analyze Sentiment"):
    if query.strip():
        tweets = fetch_tweets(query, tweet_count)
        if tweets:
            df = pd.DataFrame(tweets, columns=["Tweet"])
            df["Sentiment"] = df["Tweet"].apply(get_sentiment)
            st.dataframe(df)  # Display tweets with sentiments

            # Display sentiment distribution as a bar chart
            st.subheader("Sentiment Distribution")
            sentiment_counts = df["Sentiment"].value_counts()
            st.bar_chart(sentiment_counts)
        else:
            st.warning("No tweets fetched. Try a different keyword.")
    else:
        st.warning("Please enter a valid topic.")
