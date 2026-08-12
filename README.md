
# Customer Intelligence Analytics Platform

> **Unsupervised ML + Customer Analytics + Power BI**

An end-to-end customer intelligence platform that transforms retail transaction data into **behavioral customer segments, customer value insights, and actionable growth and retention opportunities**.

---

## 📌 Overview

Retail customers behave differently. Some customers generate significant revenue through frequent purchases, while others purchase occasionally, become inactive, or show potential for further growth.

This project uses **customer-level behavioral analytics and unsupervised machine learning** to identify these patterns and translate them into business-oriented customer segments.

The final output is an interactive **Power BI decision dashboard** designed to answer:

- Where is customer value concentrated?
- How do customer segments behave differently?
- Which customers represent growth opportunities?
- Which valuable customers are becoming dormant?
- Where should the business focus retention and growth efforts?

---

## 🔄 Project Pipeline

```text
Online Retail Transactions
          ↓
Data Cleaning & Audit
          ↓
Customer-Level Feature Engineering
          ↓
RFM + Behavioral Analysis
          ↓
Feature Scaling
          ↓
Unsupervised ML
(K-Means, GMM, DBSCAN)
          ↓
Customer Segmentation
          ↓
Customer Intelligence
          ↓
Opportunity Identification
          ↓
Power BI Dashboard
````

---

## 📊 Dataset

The project uses the **Online Retail II** transactional dataset.

The transaction-level data is aggregated to the customer level, producing approximately **5,881 customers** for behavioral analysis.

The final analytical grain is:

```text
1 row = 1 customer
```

---

## ⚙️ Customer Features

Customer behavior is represented using features including:

* Recency
* Frequency
* Monetary Value
* Average Order Value
* Average Items per Order
* Unique Products
* Active Months
* Customer Lifetime
* Average Purchase Interval
* Return Order Rate
* Return Item Rate

These features capture customer **value, engagement, purchasing behavior, and retention patterns**.

---

## 🧠 Machine Learning

Since customer segments are not predefined, the project uses **unsupervised learning**.

### Models Evaluated

* **K-Means**
* **Gaussian Mixture Models (GMM)**
* **DBSCAN**

The models were evaluated using:

* Silhouette Score
* Davies-Bouldin Index
* Calinski-Harabasz Score
* Inertia
* AIC / BIC for GMM

The final segmentation considers both **statistical performance and business interpretability**, rather than selecting a model purely from one clustering metric.

---

## 👥 Customer Segmentation

The final ML clusters were translated into business-readable customer segments:

| Segment                             | Customer Behavior                          | Business Focus              |
| ----------------------------------- | ------------------------------------------ | --------------------------- |
| 🏆 **Champions**                    | Highly engaged, frequent and high-value    | Protect & retain            |
| 💎 **High-Value Occasional Buyers** | High value but lower frequency             | Increase purchase frequency |
| 📈 **Regular Growth Customers**     | Active customers with growth potential     | Upsell & cross-sell         |
| 😴 **Dormant Customers**            | Previously active but currently disengaged | Win back                    |
| 💤 **Lost Low-Value Customers**     | Low value and long inactivity              | Minimize retention cost     |

The objective is to turn anonymous ML clusters into **meaningful customer groups that support differentiated business strategies**.

---

## 📊 RFM Analysis

RFM analysis provides an additional behavioral interpretation layer based on:

* **Recency** — How recently a customer purchased
* **Frequency** — How often a customer purchased
* **Monetary** — How much a customer spent

RFM segments provide additional context around customer quality and engagement.

The two approaches complement each other:

```text
ML Segmentation
      ↓
Discovers behavioral groups

RFM Analysis
      ↓
Explains customer engagement & value
```

---

## 🎯 Customer Intelligence

The project combines ML segmentation with behavioral and RFM information to create a customer-level intelligence layer.

Key information includes:

* Customer Segment
* RFM Segment
* Recency
* Frequency
* Monetary Value
* Average Order Value
* Customer Lifetime
* Purchase Interval
* Return Behavior
* Value Status
* Growth Opportunity
* High-Value Dormant Status

This moves the project beyond:

> **"Which cluster does this customer belong to?"**

towards:

> **"What does this customer's behavior mean for the business?"**

---

## 💡 Business Opportunities

### High-Value Dormant Customers

Customers with **high historical value but reduced recent engagement**.

These customers are prioritized for:

* Personalized win-back campaigns
* Re-engagement
* Targeted offers
* Retention efforts

---

### Growth Opportunities

Customers whose current behavior suggests potential to increase their customer value.

Potential strategies include:

* Cross-selling
* Upselling
* Increasing purchase frequency
* Product recommendations
* Loyalty progression

---

## 📈 Power BI Dashboard

The final dashboard is structured into **3 decision-focused pages**.

### 01 — Customer Portfolio

**Where is customer value concentrated?**

Includes:

* Total Customers
* Total Revenue
* Revenue per Customer
* Growth Opportunities
* Customer Share by Segment
* Revenue Share by Segment
* Revenue per Customer by Segment
* Segment-level business performance

---

### 02 — Customer Segment Intelligence

**How do the customer segments behave differently?**

Includes:

* Average Recency
* Average Frequency
* Average Order Value
* Customer Value vs Purchase Frequency
* Recency by Segment
* Frequency by Segment
* RFM/customer quality analysis
* Segment Behavioral Profile

---

### 03 — Customer Opportunity Center

**Who should the business act on?**

Focuses on:

* Growth Opportunities
* High-Value Dormant Customers
* Customer Value Status
* RFM Segments
* Customer-level behavioral metrics
* Prioritized customer lists

---

## 🗂️ Project Structure

```text
Customer-Intelligence-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning_audit.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_customer_segmentation.ipynb
│   └── 04_customer_intelligence.ipynb
│
├── models/
│
├── powerbi/
│   └── Customer_Intelligence_Dashboard.pbix
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

### Python & Analytics

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* K-Means
* Gaussian Mixture Models
* DBSCAN
* PCA
* RobustScaler

### Analytics

* RFM Analysis
* Customer Segmentation
* Behavioral Analytics
* Opportunity Analysis

### Business Intelligence

* Power BI
* DAX

---

## 🔑 Key Business Insight

Customer value is not distributed evenly across the customer base.

A relatively small group of highly engaged customers can contribute a disproportionately large share of revenue, while larger groups of dormant or low-value customers may contribute significantly less.

This makes segmentation useful for **prioritizing retention, growth, and marketing resources instead of treating every customer equally**.

---

## 🚀 Future Enhancements

* Customer churn prediction
* Predictive Customer Lifetime Value
* Dynamic customer segmentation
* Campaign response prediction
* Personalized recommendation engine
* Automated data pipeline
* Segment-level A/B testing

---

## 📌 Core Outcome

```text
Raw Transactions
       ↓
Customer Behavior
       ↓
Unsupervised Segmentation
       ↓
Customer Intelligence
       ↓
Business Opportunities
       ↓
Actionable Power BI Dashboard
```

The goal is not simply to cluster customers.

**The goal is to understand customer behavior, identify where value and opportunity exist, and help the business decide where to act.**

```
```
