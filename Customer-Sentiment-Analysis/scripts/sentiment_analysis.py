## 3️⃣ Sentiment Analysis Script (scripts/sentiment_analysis.py)

import pandas as pd
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Load Cleaned Data
df = pd.read_csv("../data/cleaned_customer_reviews.csv")

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Apply Sentiment Analysis
df["Sentiment Score"] = df["Cleaned_Review"].apply(lambda review: sia.polarity_scores(review)["compound"])
df["Sentiment Label"] = df["Sentiment Score"].apply(lambda score: "Positive" if score > 0.05 else ("Negative" if score < -0.05 else "Neutral"))

# Save Results
df.to_csv("../data/sentiment_results.csv", index=False)
print("Sentiment Analysis Completed!")