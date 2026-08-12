# Customer Intelligence & Segmentation Platform

An end-to-end customer analytics project that uses **Python, unsupervised machine learning, RFM analysis, and Power BI** to identify customer segments and translate purchasing behavior into actionable business opportunities.

---

## Overview

Retail customers have very different purchasing behaviors. Some customers generate high revenue consistently, while others purchase occasionally, become inactive, or show potential for growth.

This project analyzes transaction-level retail data and converts it into **customer-level behavioral intelligence**.

The system answers:

- Who are the most valuable customers?
- Which customers are highly engaged?
- Which customers are becoming dormant?
- Which customers have growth potential?
- How should different customer groups be treated?

---

## Project Pipeline

```text
Online Retail Transactions
          ↓
Data Cleaning & Validation
          ↓
Customer-Level Feature Engineering
          ↓
RFM & Behavioral Analysis
          ↓
Feature Scaling
          ↓
Unsupervised ML
(K-Means, GMM, DBSCAN)
          ↓
Customer Segmentation
          ↓
Customer Intelligence & Opportunity Detection
          ↓
Power BI Dashboard

```
Dataset

The project uses the Online Retail II dataset.

The transaction-level data is aggregated to the customer level, producing approximately 5,881 customers for behavioral analysis.

Customer Features

Customer behavior is represented using features such as:

Recency
Frequency
Monetary Value
Average Order Value
Average Items per Order
Unique Products
Active Months
Customer Lifetime
Average Purchase Interval
Return Order Rate
Return Item Rate

These features capture customer value, engagement, purchasing frequency, and behavior.

Machine Learning

Because customer segments are not predefined, the project uses unsupervised learning.

Models Evaluated
K-Means
Gaussian Mixture Models
DBSCAN

Models are compared using clustering metrics such as:

Silhouette Score
Davies-Bouldin Index
Calinski-Harabasz Score
Inertia
AIC / BIC for GMM

The final segmentation is selected based on both statistical quality and business interpretability, rather than relying on a single clustering metric.

Customer Segments

The final customer groups are interpreted as:

Segment	Business Meaning	Primary Objective
Champions	High-value, highly engaged customers	Protect & retain
High-Value Occasional Buyers	High spending but lower frequency	Increase purchase frequency
Regular Growth Customers	Active customers with growth potential	Upsell & cross-sell
Dormant Customers	Previously active but currently disengaged	Win back
Lost Low-Value Customers	Low historical value and long inactivity	Minimize retention cost

The machine-learning clusters are therefore converted into business-readable customer segments.

Customer Intelligence Layer

The project goes beyond clustering by combining segment information with customer behavior.

Each customer can be evaluated using:

Customer segment
RFM behavior
Recency
Frequency
Monetary value
Average Order Value
Customer lifetime
Return behavior
Value status
Growth opportunity
High-value dormant status

This allows the system to move from:

"Which cluster does this customer belong to?"

to:

"What does this customer's behavior mean
and what should the business do?"
Business Opportunities

Two important opportunity groups are identified.

High-Value Dormant Customers

Customers with significant historical value but reduced recent activity.

Recommended action: prioritize personalized win-back campaigns.

Growth Opportunities

Active customers whose purchasing behavior suggests potential to increase value.

Recommended action: cross-selling, upselling, bundling, and increasing purchase frequency.

Power BI Dashboard

The final dashboard contains three pages.

Page 1 — Customer Portfolio

Answers:

Where is customer value concentrated?

Includes:

Total Customers
Total Revenue
Revenue per Customer
Growth Opportunities
Customer Share by Segment
Revenue Share by Segment
Revenue per Customer by Segment
Segment summary
Page 2 — Segment Behavioral Intelligence

Answers:

How are the customer segments behaving differently?

Includes:

Average Recency
Average Frequency
Average Order Value
Revenue per Customer
Segment behavioral comparison
RFM/customer behavior analysis
Page 3 — Customer Opportunities

Answers:

Who should the business act on?

Focuses on:

High-value dormant customers
Growth opportunities
Customer value status
RFM segments
Customer-level behavioral metrics
Project Structure
customer-intelligence-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── customer_kmeans.pkl
│   └── customer_scaler.pkl
│
├── notebooks/
│   ├── data_understanding.ipynb
│   ├── feature.ipynb
│   ├── clustering.ipynb
│   └── customer_intelligence.ipynb
│
├── streamlit_app.py
├── requirements.txt
└── README.md
Tech Stack

Python

Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn

Machine Learning

K-Means
Gaussian Mixture Models
DBSCAN
PCA
RobustScaler

Analytics

RFM Analysis
Customer Segmentation
Behavioral Analytics
Opportunity Identification

Visualization

Power BI
Key Takeaway

This project demonstrates how unsupervised machine learning can be integrated into a practical customer analytics workflow.

Rather than treating clustering as the final result, the project transforms discovered customer patterns into:

Customer Behavior
       ↓
Segmentation
       ↓
Customer Value
       ↓
Business Opportunities
       ↓
Actionable Decisions
