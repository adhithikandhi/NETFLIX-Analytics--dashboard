import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("ℹ️ About This Project")

st.markdown("---")

# -------------------------------------------------------
# INTRODUCTION
# -------------------------------------------------------

st.header("🎬 Netflix Streaming Analytics Dashboard")

st.write("""
The **Netflix Streaming Analytics Dashboard** is an end-to-end Data Analytics
project developed using Python and Streamlit.

The goal of this project is to analyze user viewing behavior,
identify viewer drop-off patterns, explore streaming performance,
and provide business recommendations using Exploratory Data Analysis (EDA).
""")

st.markdown("---")

# -------------------------------------------------------
# PROJECT OBJECTIVES
# -------------------------------------------------------

st.header("🎯 Project Objectives")

st.markdown("""
- Analyze streaming watch history
- Measure user engagement
- Find viewer drop-off points
- Analyze device usage
- Study network performance
- Analyze customer reviews
- Perform Exploratory Data Analysis (EDA)
- Generate business insights
""")

st.markdown("---")

# -------------------------------------------------------
# TECHNOLOGY STACK
# -------------------------------------------------------

st.header("🛠️ Technology Stack")

col1, col2 = st.columns(2)

with col1:
    st.success("""
### Programming

- Python
- Pandas
- NumPy
""")

    st.success("""
### Visualization

- Plotly
- Matplotlib
- Streamlit
""")

with col2:
    st.info("""
### Data Analysis

- EDA
- Statistics
- Correlation Analysis
- Data Cleaning
""")

    st.info("""
### NLP

- TextBlob
- WordCloud
""")

st.markdown("---")

# -------------------------------------------------------
# PROJECT FEATURES
# -------------------------------------------------------

st.header("✨ Features")

features = [
    "Interactive Dashboard",
    "KPI Cards",
    "Viewer Retention Analysis",
    "Device Analysis",
    "Network Analysis",
    "Review Sentiment Analysis",
    "Word Cloud",
    "Correlation Heatmap",
    "Business Report",
    "Download Report",
]

for feature in features:
    st.write(f"✅ {feature}")

st.markdown("---")

# -------------------------------------------------------
# PROJECT STRUCTURE
# -------------------------------------------------------

st.header("📁 Project Structure")

st.code("""
Netflix-Analytics-Dashboard/
│
├── app.py
├── analysis.py
├── charts.py
├── config.py
├── data_loader.py
├── utils.py
│
├── assets/
│     └── style.css
│
├── data/
│     ├── watch_history.csv
│     ├── users.csv
│     ├── reviews.csv
│     ├── network.csv
│     └── ads.csv
│
├── pages/
│     ├── Dashboard.py
│     ├── EDA.py
│     ├── User Analysis.py
│     ├── Reviews_Analysis.py
│     ├── Business Report.py
│     └── About.py
""")

st.markdown("---")

# -------------------------------------------------------
# DASHBOARD MODULES
# -------------------------------------------------------

st.header("📊 Dashboard Modules")

modules = {
    "📊 Dashboard": "Overview of streaming performance",
    "📈 EDA": "Exploratory Data Analysis",
    "👥 User Analysis": "User demographics and watch behavior",
    "😊 Review Analysis": "Customer review sentiment",
    "📄 Business Report": "Executive summary and recommendations",
}

for module, desc in modules.items():
    st.write(f"**{module}** — {desc}")

st.markdown("---")

# -------------------------------------------------------
# BUSINESS VALUE
# -------------------------------------------------------

st.header("💼 Business Value")

st.info("""
This dashboard helps business teams:

• Increase viewer retention

• Improve customer satisfaction

• Reduce buffering issues

• Optimize advertisement placement

• Improve streaming quality

• Make data-driven decisions
""")

st.markdown("---")

# -------------------------------------------------------
# FUTURE IMPROVEMENTS
# -------------------------------------------------------

st.header("🚀 Future Improvements")

future = [
    "Machine Learning Prediction",
    "Recommendation System",
    "Real-Time Dashboard",
    "SQL Database Integration",
    "Cloud Deployment",
    "User Authentication",
    "AI Chatbot",
    "Live Streaming Analytics"
]

for item in future:
    st.write(f"🔹 {item}")

st.markdown("---")

# -------------------------------------------------------
# DEVELOPER
# -------------------------------------------------------

st.header("👨‍💻 Developer")

st.write("""
**Project:** Netflix Streaming Analytics Dashboard

**Developed Using:**
- Python
- Streamlit
- Plotly
- Pandas
- NumPy

This project demonstrates data analysis, visualization, and dashboard
development skills using modern Python tools.
""")

st.markdown("---")

st.success("🎉 Thank you for exploring the Netflix Analytics Dashboard!")