import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
}

.card{
    background:#1F2937;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.4);
    text-align:center;
}

h1,h2,h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------

st.title("🎬 Netflix Analytics Dashboard")

st.caption("Professional Streaming Analytics Dashboard")

st.divider()

# ----------------------------
# LOAD DATA
# ----------------------------

watch = pd.read_csv("data/watch_history.csv")

# ----------------------------
# KPI
# ----------------------------

total_users = watch["User_ID"].nunique()

avg_watch = round(watch["Watch_Time"].mean(),2)

completion = round((watch["Watch_Time"]>=60).mean()*100,2)

drop = round((watch["Watch_Time"]<15).mean()*100,2)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "👥 Total Users",
    total_users
)

col2.metric(
    "⏱ Avg Watch Time",
    f"{avg_watch} min"
)

col3.metric(
    "✅ Completion Rate",
    f"{completion}%"
)

col4.metric(
    "📉 Drop-off",
    f"{drop}%"
)

st.divider()

# ----------------------------
# FILTER
# ----------------------------

device = st.selectbox(
    "Select Device",
    ["All"] + sorted(list(watch["Device"].unique()))
)

if device != "All":
    watch = watch[
        watch["Device"]==device
    ]

# ----------------------------
# CHARTS
# ----------------------------

left,right = st.columns(2)

with left:

    fig = px.histogram(
        watch,
        x="Watch_Time",
        nbins=10,
        color="Device",
        title="Watch Time Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    pie = px.pie(
        watch,
        names="Device",
        hole=.6,
        title="Device Distribution",
        template="plotly_dark"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# ----------------------------
# NETWORK ANALYSIS
# ----------------------------

st.subheader("Network Usage")

network = watch.groupby(
    "Network"
).size().reset_index(name="Users")

bar = px.bar(
    network,
    x="Network",
    y="Users",
    color="Network",
    template="plotly_dark",
    text="Users"
)

st.plotly_chart(
    bar,
    use_container_width=True
)

# ----------------------------
# WATCH DATA
# ----------------------------

st.subheader("Watch History")

st.dataframe(
    watch,
    use_container_width=True
)

# ----------------------------
# INSIGHTS
# ----------------------------

st.subheader("Business Insights")

if drop > 30:

    st.error(
        "High viewer drop-off detected before video completion."
    )

if avg_watch < 30:

    st.warning(
        "Average watch time is lower than expected."
    )

st.success(
    """
Recommendations

• Improve video quality

• Reduce buffering

• Optimize advertisements

• Improve audio quality

• Personalize recommendations
"""
)