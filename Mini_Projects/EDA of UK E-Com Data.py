import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('UK E-Commerce Data.csv')

# Display the first few rows of the dataset
df.head()

# Check for missing values
df.isnull().sum()

# Check for duplicates
df.duplicated().sum()

# Check data types
df.info()

# Basic statistics
df.describe()

## Data Cleaning

# Handle missing values (if any)
# For example, if there are missing values in 'CustomerID', we might drop those rows
df = df.dropna(subset=['CustomerID'])

# Convert 'InvoiceDate' to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Check for any negative quantities (which might indicate returns)
df[df['Quantity'] < 0]

# Handle negative quantities (if necessary)
df = df[df['Quantity'] >= 0]

## Generate Insights

# Total revenue per invoice
df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']

# Total revenue by country
revenue_by_country = df.groupby('Country')['TotalRevenue'].sum().sort_values(ascending=False)
revenue_by_country

# Top 10 customers by revenue
top_customers = df.groupby('CustomerID')['TotalRevenue'].sum().sort_values(ascending=False).head(10)
top_customers

# Most popular products
popular_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
popular_products

# Sales trend over time
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('InvoiceMonth')['TotalRevenue'].sum()

## Data Visualization

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Plot total revenue by country
plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_by_country.index, y=revenue_by_country.values, palette="viridis")
plt.title('Total Revenue by Country')
plt.xlabel('Country')
plt.ylabel('Total Revenue')
plt.xticks(rotation=90)
plt.tight_layout()  # To make sure the labels fit
plt.savefig('total_revenue_by_country.png')  # Save the plot
plt.show()

# Plot top 10 customers by revenue
plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.index, y=top_customers.values, palette="magma")
plt.title('Top 10 Customers by Revenue')
plt.xlabel('Customer ID')
plt.ylabel('Total Revenue')
plt.tight_layout()  # To make sure the labels fit
plt.savefig('top_10_customers_by_revenue.png')  # Save the plot
plt.show()

# Plot most popular products
plt.figure(figsize=(10, 6))
sns.barplot(x=popular_products.index, y=popular_products.values, palette="plasma")
plt.title('Most Popular Products by Quantity Sold')
plt.xlabel('Product Description')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=90)
plt.tight_layout()  # To make sure the labels fit
plt.savefig('most_popular_products.png')  # Save the plot
plt.show()

# Plot monthly sales trend
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.tight_layout()  # To make sure the labels fit
plt.savefig('monthly_sales_trend.png')  # Save the plot
plt.show()


## Summary of Findings

### Data Overview
####- The dataset contains information about e-commerce transactions, including invoice details, product descriptions, quantities, prices,# customer IDs, and countries.
####- There were some missing values in the 'CustomerID' column, which were dropped.
####- The 'InvoiceDate' column was converted to datetime format for time-based analysis.

### Key Insights
####- **Revenue by Country**: The United Kingdom dominates in terms of total revenue, followed by Germany and France.
####- **Top Customers**: The top 10 customers contribute significantly to the total revenue.
####- **Popular Products**: Certain products are more popular than others, with high quantities sold.
####- **Sales Trend**: There is a noticeable trend in monthly sales, with peaks and troughs that could be analyzed further for seasonality.

### Visualizations
####- **Bar Charts**: Used to visualize total revenue by country, top customers, and popular products.
####- **Line Plot**: Used to show the monthly sales trend over time.

### Conclusion
####- The dataset provides valuable insights into customer behavior, product popularity, and sales trends.
####- Further analysis could involve customer segmentation, product recommendation systems, and predictive modeling for sales forecasting.
