# 📊 E-Commerce Data Analysis

## 📌 Overview
This project performs **Exploratory Data Analysis (EDA)** on an **E-commerce dataset** containing transaction details such as invoices, products, customer IDs, and sales revenue.

## 📂 Dataset Details
- **Dataset Name:** UK E-Commerce Data
- **Rows Analyzed:** First 2000 rows
- **Key Columns:**
  - InvoiceNo (Transaction ID)
  - StockCode (Product ID)
  - Description (Product Name)
  - Quantity (Number of units sold)
  - InvoiceDate (Date of transaction)
  - UnitPrice (Price per unit)
  - CustomerID (Unique customer identifier)
  - Country (Customer's country)

## 🔍 Steps Performed

### 1️⃣ **Data Cleaning** 🛠️
- Checked for **missing values** and removed rows with missing `CustomerID`.
- Converted `InvoiceDate` to **datetime format**.
- Identified and removed transactions with **negative quantities** (possible returns).

### 2️⃣ **Generating Insights** 📊
- **Total Revenue per Invoice**: Computed `TotalRevenue = Quantity * UnitPrice`.
- **Revenue by Country**: Identified countries with the highest revenue.
- **Top Customers**: Ranked customers based on total spending.
- **Most Popular Products**: Analyzed which products were sold the most.
- **Sales Trends Over Time**: Examined revenue patterns month by month.

### 3️⃣ **Data Visualization** 📈
- **Total Revenue by Country** (Bar Chart) 🌍
- **Top 10 Customers by Revenue** (Bar Chart) 💰
- **Most Popular Products** (Bar Chart) 🛒
- **Monthly Sales Trends** (Line Plot) 📆

## 🔥 Key Findings
- 🇬🇧 **United Kingdom** generates the highest revenue, followed by **Germany** and **France**.
- The **top 10 customers** significantly contribute to total sales.
- Some products are much more **popular** than others.
- **Monthly sales trends** show peaks and troughs, possibly indicating seasonal effects.

## 🚀 Future Work
- Customer segmentation for better marketing strategies.
- Predictive modeling for **sales forecasting**.
- Implementing a **recommendation system** for personalized shopping experiences.

💡 **Want to explore more?** Check out the Jupyter Notebook for full code and visualizations!

---
✍️ *Created by [T Venkatakrishna Tharanikanti]*

