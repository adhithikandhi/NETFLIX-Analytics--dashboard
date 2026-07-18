import streamlit as st

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

def load_css():
    try:
        with open("assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("CSS file not found.")

load_css()

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
    width=180
)

st.sidebar.success("🎬 Netflix Analytics Dashboard")

st.sidebar.markdown("""
### 📂 Navigation

Use the pages below to explore:

- 📊 Dashboard
- 📈 EDA
- 👥 User Analysis
- 😊 Review Analysis
- 📄 Business Report
- ℹ️ About
""")

# -------------------------------------------------------
# HOME PAGE
# -------------------------------------------------------

st.title("🎬 Netflix Analytics Dashboard")

st.markdown("""
### Streaming Content Optimization using Exploratory Data Analysis (EDA)

Welcome to the **Netflix Analytics Dashboard**.

This project demonstrates how Exploratory Data Analysis (EDA) helps understand viewer behavior, identify content issues, and generate business insights.

Use the **left sidebar** to navigate through the different analysis pages.
""")

st.divider()

# -------------------------------------------------------
# KPI CARDS
# -------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Users",
        "25,420",
        "+12%"
    )

with col2:
    st.metric(
        "⏱ Average Watch Time",
        "42.6 min",
        "+3.5%"
    )

with col3:
    st.metric(
        "📉 Drop-off Rate",
        "38%",
        "-8%"
    )

with col4:
    st.metric(
        "⭐ Average Rating",
        "4.7 / 5",
        "+0.2"
    )

st.divider()

# -------------------------------------------------------
# PROJECT OVERVIEW
# -------------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🎯 Project Objective")

    st.info("""
This dashboard helps identify why users stop watching videos before completion.

The analysis includes:

- Viewer Retention
- Watch Time Analysis
- Device Performance
- Network Analysis
- User Reviews
- Business Insights
""")

with right:

    st.subheader("✨ Features")

    st.success("""
✔ Interactive Dashboard

✔ Exploratory Data Analysis (EDA)

✔ User Analysis

✔ Review Sentiment Analysis

✔ Business Report

✔ Interactive Plotly Charts

✔ Download Reports

✔ Professional UI
""")

st.divider()

# -------------------------------------------------------
# TECHNOLOGY STACK
# -------------------------------------------------------

st.subheader("🛠️ Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown("""
### Python Libraries

- Pandas
- NumPy
- Streamlit
""")

with tech2:
    st.markdown("""
### Visualization

- Plotly
- Matplotlib
- WordCloud
""")

with tech3:
    st.markdown("""
### Analytics

- EDA
- TextBlob
- Business Intelligence
""")

st.divider()

# -------------------------------------------------------
# PROJECT WORKFLOW
# -------------------------------------------------------

st.subheader("📊 Dashboard Workflow")

st.markdown("""
1. 📥 Load Streaming Data

2. 🧹 Clean & Prepare Data

3. 📈 Perform Exploratory Data Analysis

4. 👥 Analyze User Behavior

5. 😊 Analyze User Reviews

6. 📄 Generate Business Report

7. 💡 Provide Business Recommendations
""")

st.divider()

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.markdown(
    """
---
<center>

### 🎬 Netflix Analytics Dashboard

Developed using **Python • Streamlit • Plotly • Pandas**

</center>
""",
    unsafe_allow_html=True
) 