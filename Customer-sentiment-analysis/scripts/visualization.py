## 4️⃣ Data Visualization Script (scripts/visualization.py)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("../data/sentiment_results.csv")

# Sentiment Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sentiment Label", palette="coolwarm")
plt.title("Customer Sentiment Distribution")
plt.savefig("../data/sentiment_distribution.png")
plt.show()
