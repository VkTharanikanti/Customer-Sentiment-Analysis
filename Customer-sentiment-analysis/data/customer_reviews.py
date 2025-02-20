## 1️⃣ Create & Load Customer Reviews Dataset (data/customer_reviews.csv)

import pandas as pd
import random
from faker import Faker

fake = Faker()
reviews = [
    "Great product, very useful!",
    "Terrible quality, broke quickly.",
    "Average, nothing special.",
    "Highly recommend this!",
    "Not worth the money.",
    "Excellent service and fast delivery!",
    "Very disappointed, poor design.",
]

data = []
for _ in range(500):
    data.append([
        fake.uuid4(),
        fake.name(),
        random.choice(reviews),
        random.randint(1, 5),
        fake.date_this_year()
    ])

df = pd.DataFrame(data, columns=["Review_ID", "Customer", "Review", "Rating", "Date"])
df.to_csv("customer_reviews.csv", index=False)
print("Sample dataset created!")