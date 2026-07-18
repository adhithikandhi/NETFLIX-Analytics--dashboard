import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Business Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Business Intelligence Report")

st.caption("Executive Summary for Streaming Analytics")

st.markdown("---")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

watch = pd.read_csv("data/watch_history.csv")
users = pd.read_csv("data/users.csv")
reviews = pd.read_csv("data/reviews.csv")

df = pd.merge(watch, users, on="User_ID")

# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------

total_users = df["User_ID"].nunique()
avg_watch = round(df["Watch_Time"].mean(),2)
completion = round((df["Watch_Time"]>=60).mean()*100,2)
dropoff = round((df["Watch_Time"]<15).mean()*100,2)

c1,c2,c3,c4 = st.columns(4)

c1.metric("👥 Users", total_users)
c2.metric("⏱ Avg Watch", f"{avg_watch} min")
c3.metric("✅ Completion", f"{completion}%")
c4.metric("📉 Drop-off", f"{dropoff}%")

st.markdown("---")

# -------------------------------------------------
# EXECUTIVE SUMMARY
# -------------------------------------------------

st.header("📋 Executive Summary")

st.info(f"""

### Project Objective

Analyze viewer behavior and identify why users stop watching videos.

### Key Findings

• Total Users: **{total_users}**

• Average Watch Time: **{avg_watch} minutes**

• Completion Rate: **{completion}%**

• Drop-off Rate: **{dropoff}%**

### Business Impact

Reducing the drop-off rate can significantly improve viewer engagement,
advertisement revenue, and customer retention.

""")

# -------------------------------------------------
# DEVICE PERFORMANCE
# -------------------------------------------------

st.header("📱 Device Performance")

device = (
    df.groupby("Device")["Watch_Time"]
    .mean()
    .reset_index()
)

fig = px.bar(
    device,
    x="Device",
    y="Watch_Time",
    color="Device",
    text_auto=True,
    template="plotly_dark",
    title="Average Watch Time by Device"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# COUNTRY ANALYSIS
# -------------------------------------------------

st.header("🌍 Country Analysis")

country = (
    df.groupby("Country")["Watch_Time"]
    .mean()
    .reset_index()
)

country_fig = px.bar(
    country,
    x="Country",
    y="Watch_Time",
    color="Country",
    text_auto=True,
    template="plotly_dark"
)

st.plotly_chart(country_fig, use_container_width=True)

# -------------------------------------------------
# AGE GROUP ANALYSIS
# -------------------------------------------------

st.header("🎂 Age Group Analysis")

bins = [18,25,35,45,60]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-60"
]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

age = (
    df.groupby("Age Group")
    .size()
    .reset_index(name="Users")
)

age_chart = px.pie(
    age,
    names="Age Group",
    values="Users",
    hole=.6,
    template="plotly_dark"
)

st.plotly_chart(age_chart, use_container_width=True)

# -------------------------------------------------
# SWOT ANALYSIS
# -------------------------------------------------

st.header("📊 SWOT Analysis")

left,right = st.columns(2)

with left:

    st.success("""
### Strengths

✔ High completion rate on TV

✔ Positive user engagement

✔ Large active user base
""")

    st.warning("""
### Weaknesses

• Mobile buffering

• Audio issues

• Advertisement timing
""")

with right:

    st.info("""
### Opportunities

✔ AI Recommendation Engine

✔ Personalized Content

✔ Better Streaming Quality
""")

    st.error("""
### Threats

• Competitors

• User Churn

• Poor Reviews
""")

# -------------------------------------------------
# FINAL RECOMMENDATIONS
# -------------------------------------------------

st.header("🚀 Recommendations")

recommendations = [
    "Improve mobile streaming quality",
    "Reduce buffering on low-speed networks",
    "Optimize advertisement placement",
    "Improve subtitle synchronization",
    "Use AI for personalized recommendations",
    "Compress large video segments",
    "Monitor viewer retention in real-time",
    "Analyze reviews weekly",
    "Improve audio quality",
    "Launch A/B testing for advertisements"
]

for i, item in enumerate(recommendations, start=1):
    st.write(f"{i}. {item}")

# -------------------------------------------------
# DOWNLOAD REPORT
# -------------------------------------------------

st.header("📥 Download Report")

report = f"""
NETFLIX ANALYTICS REPORT

Generated:
{datetime.now()}

Total Users : {total_users}

Average Watch Time : {avg_watch}

Completion Rate : {completion}

Drop-off Rate : {dropoff}

Business Recommendations

- Improve Streaming
- Better Audio
- Reduce Buffering
- AI Recommendation System
"""

st.download_button(
    label="⬇ Download Report",
    data=report,
    file_name="Netflix_Analytics_Report.txt",
    mime="text/plain"
)

st.markdown("---")

st.success("✅ Business Report Generated Successfully")