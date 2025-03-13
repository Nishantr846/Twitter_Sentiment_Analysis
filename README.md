# Twitter Sentiment Analysis using Streamlit & Tweepy

## Overview
This project is a **Twitter Sentiment Analysis** web application built using **Streamlit** and **Tweepy**. It fetches recent tweets on a given topic and analyzes their sentiment using **TextBlob**. The sentiment is classified as **Positive, Negative, or Neutral** and displayed in a tabular format along with a sentiment distribution chart.

## Features
- Fetches real-time tweets using **Twitter API v2**
- Performs **sentiment analysis** using **TextBlob**
- Displays tweets along with their sentiment classification
- Provides an interactive **bar chart** for sentiment distribution

## Installation

### 1. Clone the Repository
git clone https://github.com/Nishantr846/Twitter_Sentiment_Analysis

### 2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows

### 3. Install Dependencies
pip install -r requirements.txt


### 4. Set Up Twitter API Credentials
Create a `.env` file in the root directory and add your Twitter **BEARER_TOKEN**:
BEARER_TOKEN=your_twitter_bearer_token

## Running the Application

streamlit run textblob_sentiment.py

After running the above command, Streamlit will generate a local **URL** (e.g., `http://localhost:8501`). Open it in your browser.

## Usage
1. Enter a **keyword or topic** in the text box (e.g., `Bitcoin`, `Elon Musk`, `AI`)
2. Select the **number of tweets** to fetch using the slider
3. Click **Analyze Sentiment**
4. View fetched tweets with their sentiment classification
5. Check the sentiment distribution chart

## Dependencies
- **Streamlit** (UI framework)
- **Tweepy** (Twitter API integration)
- **TextBlob** (Sentiment analysis)
- **Pandas** (Data processing)
- **Python-dotenv** (Environment variable management)

## Contribution
Feel free to submit issues or contribute by making a pull request!

## Author
Developed by **Nishant**
Email - nishantr846@gmail.com
LinkedIn - https://www.linkedin.com/in/nishantr846/

