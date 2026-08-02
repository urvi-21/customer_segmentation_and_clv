import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#0F172A;
}

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

h1,h2,h3{
    color:white;
}

div[data-testid="stMetric"]{

    background:#1E293B;

    border-radius:15px;

    padding:15px;

    border:1px solid #334155;

}

section[data-testid="stSidebar"]{

    background:#111827;

}

</style>
""",unsafe_allow_html=True)

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

@st.cache_data
def load_data():

    customer = pd.read_csv(
        "data/processed/customer_intelligence.csv"
    )

    features = pd.read_csv(
        "data/processed/customer_features.csv"
    )

    segments = pd.read_csv(
        "data/processed/customer_segments.csv"
    )

    churn = pd.read_csv(
        "data/processed/churn_predictions.csv"
    )

    clv = pd.read_csv(
        "data/processed/clv_predictions.csv"
    )

    return customer,features,segments,churn,clv


customer_df,features,segments,churn,clv=load_data()


# ----------------------------------------------------
# TITLE
# ----------------------------------------------------

st.title("📊 Customer Intelligence Platform")

st.caption(
"""
Customer Segmentation • Churn Prediction • Customer Lifetime Value
"""
)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("Dashboard Filters")

country_options=["All"]+sorted(
    customer_df["country"].dropna().unique().tolist()
)

segment_options=["All"]+sorted(
    customer_df["segment"].dropna().unique().tolist()
)

risk_options=["All"]+sorted(
    customer_df["Risk_Level"].dropna().unique().tolist()
)

clv_options=["All"]+sorted(
    customer_df["CLV_Category"].dropna().unique().tolist()
)

country=st.sidebar.selectbox(
    "Country",
    country_options
)

segment=st.sidebar.selectbox(
    "Segment",
    segment_options
)

risk=st.sidebar.selectbox(
    "Risk Level",
    risk_options
)

clv_cat=st.sidebar.selectbox(
    "CLV Category",
    clv_options
)

# ----------------------------------------------------
# FILTER DATA
# ----------------------------------------------------

filtered=customer_df.copy()

if country!="All":
    filtered=filtered[
        filtered["country"]==country
    ]

if segment!="All":
    filtered=filtered[
        filtered["segment"]==segment
    ]

if risk!="All":
    filtered=filtered[
        filtered["Risk_Level"]==risk
    ]

if clv_cat!="All":
    filtered=filtered[
        filtered["CLV_Category"]==clv_cat
    ]

# ----------------------------------------------------
# KPI CARDS
# ----------------------------------------------------

kpi1,kpi2,kpi3,kpi4,kpi5,kpi6=st.columns(6)

kpi1.metric(
    "Customers",
    f"{len(filtered):,}"
)

kpi2.metric(
    "Avg CLV",
    f"${filtered['Predicted_CLV'].mean():,.0f}"
)

kpi3.metric(
    "Avg Health",
    f"{filtered['health_score'].mean():.1f}"
)

kpi4.metric(
    "High Risk",
    (filtered["Risk_Level"]=="High").sum()
)

kpi5.metric(
    "Critical",
    (filtered["Risk_Level"]=="Critical").sum()
)

kpi6.metric(
    "VIP",
    (filtered["CLV_Category"]=="VIP").sum()
)

st.divider()

# ----------------------------------------------------
# INTERACTIVE CHARTS
# ----------------------------------------------------

row1_col1, row1_col2 = st.columns(2)

# ----------------------------------------------------
# CUSTOMER SEGMENTS
# ----------------------------------------------------

with row1_col1:

    st.subheader("👥 Customer Segments")

    segment_chart = (
        filtered["segment"]
        .value_counts()
        .reset_index()
    )

    segment_chart.columns = [
        "Segment",
        "Customers"
    ]

    fig = px.pie(
        segment_chart,
        names="Segment",
        values="Customers",
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        height=420,
        template="plotly_dark",
        margin=dict(l=20,r=20,t=40,b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# CHURN RISK
# ----------------------------------------------------

with row1_col2:

    st.subheader("⚠️ Churn Risk Distribution")

    risk_chart = (
        filtered["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    risk_chart.columns = [
        "Risk",
        "Customers"
    ]

    fig = px.bar(
        risk_chart,
        x="Risk",
        y="Customers",
        color="Risk",
        text_auto=True,
        color_discrete_sequence=px.colors.sequential.Reds
    )

    fig.update_layout(
        height=420,
        template="plotly_dark",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# SECOND ROW
# ----------------------------------------------------

row2_col1, row2_col2 = st.columns(2)

# ----------------------------------------------------
# CLV DISTRIBUTION
# ----------------------------------------------------

with row2_col1:

    st.subheader("💰 Predicted CLV")

    fig = px.histogram(
        filtered,
        x="Predicted_CLV",
        nbins=40,
        color_discrete_sequence=["#00CC96"]
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# HEALTH SCORE
# ----------------------------------------------------

with row2_col2:

    st.subheader("❤️ Customer Health Score")

    fig = px.histogram(
        filtered,
        x="health_score",
        nbins=25,
        color_discrete_sequence=["#636EFA"]
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# THIRD ROW
# ----------------------------------------------------

row3_col1, row3_col2 = st.columns(2)

# ----------------------------------------------------
# CLV CATEGORY
# ----------------------------------------------------

with row3_col1:

    st.subheader("🏆 CLV Categories")

    clv_chart = (
        filtered["CLV_Category"]
        .value_counts()
        .reset_index()
    )

    clv_chart.columns = [
        "Category",
        "Customers"
    ]

    fig = px.bar(
        clv_chart,
        x="Category",
        y="Customers",
        text_auto=True,
        color="Category",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig.update_layout(
        template="plotly_dark",
        height=420,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------
# BUSINESS PRIORITY
# ----------------------------------------------------

with row3_col2:

    st.subheader("📈 Business Priority")

    priority = (
        filtered["Priority_Level"]
        .value_counts()
        .reset_index()
    )

    priority.columns = [
        "Priority",
        "Customers"
    ]

    fig = px.funnel(
        priority,
        x="Customers",
        y="Priority",
        color="Priority",
        color_discrete_sequence=px.colors.sequential.Plasma
    )

    fig.update_layout(
        template="plotly_dark",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ----------------------------------------------------
# CUSTOMER INTELLIGENCE TABLE
# ----------------------------------------------------

st.header("🧠 Customer Intelligence")

search = st.text_input(
    "🔍 Search Customer ID"
)

display_df = filtered.copy()

if search != "":
    try:
        customer_id = int(search)

        display_df = display_df[
            display_df["customer_id"] == customer_id
        ]

    except:
        st.warning("Enter a valid Customer ID")

st.dataframe(
    display_df[
        [
            "customer_id",
            "segment",
            "Risk_Level",
            "Predicted_CLV",
            "health_score",
            "Business_Priority",
            "Recommended_Action"
        ]
    ],
    use_container_width=True,
    height=350
)

st.divider()

# ----------------------------------------------------
# CUSTOMER 360
# ----------------------------------------------------

st.header("👤 Customer 360")

customer_ids = sorted(
    filtered["customer_id"].unique()
)

selected_customer = st.selectbox(
    "Select Customer",
    customer_ids
)

customer = filtered[
    filtered["customer_id"] == selected_customer
].iloc[0]

left, right = st.columns([1,2])

# ----------------------------------------------------
# CUSTOMER METRICS
# ----------------------------------------------------

with left:

    st.metric(
        "Customer ID",
        int(customer["customer_id"])
    )

    st.metric(
        "Segment",
        customer["segment"]
    )

    st.metric(
        "Risk",
        customer["Risk_Level"]
    )

    st.metric(
        "Health Score",
        f"{customer['health_score']:.1f}"
    )

    st.metric(
        "Predicted CLV",
        f"${customer['Predicted_CLV']:,.0f}"
    )

# ----------------------------------------------------
# CUSTOMER DETAILS
# ----------------------------------------------------

with right:

    st.subheader("Customer Profile")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Purchase Behaviour")

        st.write(
            f"**Recency:** {customer['recency']:.0f} days"
        )

        st.write(
            f"**Frequency:** {customer['frequency']:.0f}"
        )

        st.write(
            f"**Monetary:** ${customer['monetary']:,.2f}"
        )

        st.write(
            f"**Average Basket Size:** {customer['avg_basket_size']:.2f}"
        )

        st.write(
            f"**Active Months:** {customer['active_months']:.0f}"
        )

    with col2:

        st.write("### Customer Intelligence")

        st.write(
            f"**Business Priority:** {customer['Priority_Level']}"
        )

        st.write(
            f"**Churn Probability:** {customer['Churn_Probability']:.2%}"
        )

        st.write(
            f"**CLV Category:** {customer['CLV_Category']}"
        )

        st.write(
            f"**Return Rate:** {customer['return_rate']:.2%}"
        )

        st.write(
            f"**Country:** {customer['country']}"
        )

st.divider()

# ----------------------------------------------------
# RECOMMENDED ACTION
# ----------------------------------------------------

st.header("🎯 Recommended Business Action")

st.success(customer["Recommended_Action"])

# ----------------------------------------------------
# CUSTOMER HEALTH GAUGE
# ----------------------------------------------------

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=customer["health_score"],

    title={"text":"Customer Health Score"},

    gauge={

        "axis":{"range":[0,100]},

        "bar":{"color":"limegreen"},

        "steps":[

            {"range":[0,40],"color":"red"},

            {"range":[40,70],"color":"orange"},

            {"range":[70,100],"color":"green"}

        ]

    }

))

fig.update_layout(
    template="plotly_dark",
    height=350
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()


# ----------------------------------------------------
# EXECUTIVE INSIGHTS
# ----------------------------------------------------

st.header("📈 Executive Insights")

col1, col2 = st.columns(2)

# ----------------------------------------------------
# TOP VIP CUSTOMERS
# ----------------------------------------------------

with col1:

    st.subheader("🏆 Top 10 VIP Customers")

    vip = (
        filtered
        .sort_values(
            "Predicted_CLV",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        vip[
            [
                "customer_id",
                "segment",
                "Predicted_CLV",
                "health_score"
            ]
        ],
        use_container_width=True
    )

# ----------------------------------------------------
# HIGH RISK CUSTOMERS
# ----------------------------------------------------

with col2:

    st.subheader("⚠️ Top High-Risk Customers")

    risk = (
        filtered
        .sort_values(
            "Churn_Probability",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        risk[
            [
                "customer_id",
                "Risk_Level",
                "Churn_Probability",
                "Predicted_CLV"
            ]
        ],
        use_container_width=True
    )

st.divider()

# ----------------------------------------------------
# BUSINESS OPPORTUNITIES
# ----------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("💰 Upsell Opportunities")

    upsell = filtered[
        (filtered["Predicted_CLV"] > filtered["Predicted_CLV"].median()) &
        (filtered["Churn_Probability"] < 0.30)
    ]

    st.metric(
        "Customers",
        len(upsell)
    )

    st.dataframe(
        upsell[
            [
                "customer_id",
                "segment",
                "Predicted_CLV"
            ]
        ].head(10),
        use_container_width=True
    )

with right:

    st.subheader("❤️ Retention Opportunities")

    retention = filtered[
        (filtered["Churn_Probability"] > 0.70)
    ]

    st.metric(
        "Customers",
        len(retention)
    )

    st.dataframe(
        retention[
            [
                "customer_id",
                "Risk_Level",
                "Predicted_CLV"
            ]
        ].head(10),
        use_container_width=True
    )

st.divider()

# ----------------------------------------------------
# DOWNLOAD RESULTS
# ----------------------------------------------------

st.header("⬇️ Export Results")

download_df = filtered.copy()

csv = download_df.to_csv(index=False).encode("utf-8")

st.download_button(

    label="Download Customer Intelligence Report",

    data=csv,

    file_name="customer_intelligence.csv",

    mime="text/csv"

)

st.divider()

# ----------------------------------------------------
# MODEL PERFORMANCE
# ----------------------------------------------------

with st.expander("🤖 Model Performance"):

    metrics = pd.DataFrame({

        "Model":[

            "Customer Segmentation",

            "Churn Prediction",

            "CLV Prediction"

        ],

        "Algorithm":[

            "KMeans",

            "Random Forest",

            "Random Forest"

        ],

        "Performance":[

            "4 Clusters",

            "ROC-AUC = 0.79",

            "R² = 0.47"

        ]

    })

    st.table(metrics)

st.divider()

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown(
"""
---
### 📊 Customer Intelligence Platform

Built with:

- Python
- Pandas
- Scikit-learn
- XGBoost
- Plotly
- Streamlit

Modules Included:

- Customer Segmentation
- Churn Prediction
- Customer Lifetime Value Prediction
- Customer Intelligence Engine
- Business Recommendation System

© 2026
"""
)