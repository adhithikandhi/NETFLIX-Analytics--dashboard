import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="User Analysis",
    page_icon="👥",
    layout="wide"
)

st.title("👥 User Analysis Dashboard")

st.markdown("---")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

watch = pd.read_csv("data/watch_history.csv")
users = pd.read_csv("data/users.csv")

# Merge datasets
df = pd.merge(
    watch,
    users,
    on="User_ID",
    how="left"
)

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Country",
    options=sorted(df["Country"].dropna().unique()),
    default=sorted(df["Country"].dropna().unique())
)

gender = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["Gender"].dropna().unique()),
    default=sorted(df["Gender"].dropna().unique())
)

device = st.sidebar.multiselect(
    "Device",
    options=sorted(df["Device"].dropna().unique()),
    default=sorted(df["Device"].dropna().unique())
)

filtered = df[
    (df["Country"].isin(country)) &
    (df["Gender"].isin(gender)) &
    (df["Device"].isin(device))
]

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

total_users = filtered["User_ID"].nunique()
avg_age = round(filtered["Age"].mean(), 1)
avg_watch = round(filtered["Watch_Time"].mean(), 1)
completion = round((filtered["Watch_Time"] >= 60).mean() * 100, 1)

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Users", total_users)
c2.metric("🎂 Avg Age", avg_age)
c3.metric("⏱ Avg Watch", f"{avg_watch} min")
c4.metric("✅ Completion", f"{completion}%")

st.markdown("---")

# ---------------------------------------------------
# COUNTRY ANALYSIS
# ---------------------------------------------------

left, right = st.columns(2)

with left:

    country_df = (
        filtered["Country"]
        .value_counts()
        .reset_index()
    )

    country_df.columns = ["Country", "Users"]

    fig = px.bar(
        country_df,
        x="Country",
        y="Users",
        color="Country",
        text="Users",
        template="plotly_dark",
        title="Users by Country"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    gender_df = (
        filtered["Gender"]
        .value_counts()
        .reset_index()
    )

    gender_df.columns = ["Gender", "Users"]

    pie = px.pie(
        gender_df,
        names="Gender",
        values="Users",
        hole=0.55,
        template="plotly_dark",
        title="Gender Distribution"
    )

    st.plotly_chart(pie, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# AGE DISTRIBUTION
# ---------------------------------------------------

st.subheader("🎂 Age Distribution")

hist = px.histogram(
    filtered,
    x="Age",
    nbins=10,
    color="Gender",
    template="plotly_dark"
)

st.plotly_chart(hist, use_container_width=True)

# ---------------------------------------------------
# WATCH TIME BY AGE
# ---------------------------------------------------

st.subheader("⏱ Watch Time vs Age")

scatter = px.scatter(
    filtered,
    x="Age",
    y="Watch_Time",
    color="Device",
    size="Watch_Time",
    hover_data=["Country"],
    template="plotly_dark"
)

st.plotly_chart(scatter, use_container_width=True)

# ---------------------------------------------------
# DEVICE ANALYSIS
# ---------------------------------------------------

st.subheader("📱 Device Analysis")

device_df = (
    filtered["Device"]
    .value_counts()
    .reset_index()
)

device_df.columns = ["Device", "Users"]

donut = px.pie(
    device_df,
    names="Device",
    values="Users",
    hole=.60,
    template="plotly_dark"
)

st.plotly_chart(donut, use_container_width=True)

# ---------------------------------------------------
# TOP USERS
# ---------------------------------------------------

st.subheader("🏆 Top Watch Time")

top = filtered.sort_values(
    by="Watch_Time",
    ascending=False
)

st.dataframe(
    top,
    use_container_width=True
)

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.subheader("📋 Business Insights")

highest_country = country_df.iloc[0]["Country"]

highest_device = device_df.iloc[0]["Device"]

st.success(f"Highest Users: {highest_country}")

st.success(f"Most Popular Device: {highest_device}")

st.info("""
Recommendations

• Improve streaming quality for mobile users

• Personalize recommendations by country

• Create age-based content suggestions

• Improve user engagement

• Optimize advertisement placement
""") 