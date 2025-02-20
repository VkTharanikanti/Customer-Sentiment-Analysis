## 2️⃣ Data Cleaning Script (scripts/data_cleaning.py)

import pandas as pd
import re

# Load Data
df = pd.read_csv("../data/customer_reviews.csv")

# Convert Date Column to DateTime
df["Date"] = pd.to_datetime(df["Date"])

# Remove Duplicates
df.drop_duplicates(subset=["Review"], inplace=True)

# Clean Text (Remove special characters)
df["Cleaned_Review"] = df["Review"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x.lower()))

# Save Cleaned Data
df.to_csv("../data/cleaned_customer_reviews.csv", index=False)
print("Data Cleaning Completed!")
