## 5️⃣ Interactive Dashboard (dashboard/app.py)

import pandas as pd
import streamlit as st

# Load Data
df = pd.read_csv("../data/sentiment_results.csv")

st.title("🛒 Customer Sentiment Analysis Dashboard")

# Sentiment Summary
st.metric("Total Reviews", len(df))
st.metric("Positive Reviews", len(df[df["Sentiment Label"] == "Positive"]))
st.metric("Negative Reviews", len(df[df["Sentiment Label"] == "Negative"]))

# Sentiment Distribution
st.subheader("🔹 Sentiment Breakdown")
sentiment_counts = df["Sentiment Label"].value_counts()
st.bar_chart(sentiment_counts)

# Display Sample Reviews
st.subheader("🔍 Sample Reviews")
st.dataframe(df[["Customer", "Review", "Sentiment Label"]].sample(5))

# Run using: `streamlit run dashboard/app.py`