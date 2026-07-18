import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="EDA",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Exploratory Data Analysis")

st.markdown("---")

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv("data/watch_history.csv")

# ----------------------------------
# DATASET PREVIEW
# ----------------------------------

st.subheader("Dataset Preview")

st.dataframe(df, use_container_width=True)

# ----------------------------------
# SHAPE
# ----------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.markdown("---")

# ----------------------------------
# DATA TYPES
# ----------------------------------

st.subheader("Column Data Types")

dtype = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype, use_container_width=True)

# ----------------------------------
# MISSING VALUES
# ----------------------------------

st.subheader("Missing Values")

missing = df.isnull().sum().reset_index()

missing.columns = ["Column", "Missing Values"]

fig = px.bar(
    missing,
    x="Column",
    y="Missing Values",
    color="Missing Values",
    text="Missing Values",
    template="plotly_dark",
    title="Missing Values Analysis"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----------------------------------
# NUMERICAL SUMMARY
# ----------------------------------

st.subheader("Statistical Summary")

st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

# ----------------------------------
# HISTOGRAM
# ----------------------------------

st.subheader("Watch Time Distribution")

hist = px.histogram(
    df,
    x="Watch_Time",
    nbins=10,
    color="Device",
    template="plotly_dark"
)

st.plotly_chart(hist, use_container_width=True)

# ----------------------------------
# BOXPLOT
# ----------------------------------

st.subheader("Outlier Detection")

box = px.box(
    df,
    y="Watch_Time",
    color="Device",
    template="plotly_dark"
)

st.plotly_chart(box, use_container_width=True)

# ----------------------------------
# DEVICE COUNT
# ----------------------------------

st.subheader("Device Distribution")

device = df["Device"].value_counts().reset_index()

device.columns = ["Device", "Users"]

pie = px.pie(
    device,
    names="Device",
    values="Users",
    hole=0.55,
    template="plotly_dark"
)

st.plotly_chart(pie, use_container_width=True)

# ----------------------------------
# NETWORK COUNT
# ----------------------------------

st.subheader("Network Distribution")

network = df["Network"].value_counts().reset_index()

network.columns = ["Network", "Users"]

bar = px.bar(
    network,
    x="Network",
    y="Users",
    color="Network",
    text="Users",
    template="plotly_dark"
)

st.plotly_chart(bar, use_container_width=True)

# ----------------------------------
# CORRELATION
# ----------------------------------

st.subheader("Correlation Heatmap")

corr = df.select_dtypes(include="number").corr()

fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    annotation_text=round(corr,2).values,
    colorscale="Viridis",
    showscale=True
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------
# COMPLETION RATE
# ----------------------------------

st.subheader("Completion Rate")

completed = len(df[df["Watch_Time"] >= 60])

not_completed = len(df[df["Watch_Time"] < 60])

completion = pd.DataFrame({
    "Status":["Completed","Dropped"],
    "Users":[completed,not_completed]
})

donut = px.pie(
    completion,
    names="Status",
    values="Users",
    hole=0.60,
    color="Status",
    color_discrete_map={
        "Completed":"green",
        "Dropped":"red"
    },
    template="plotly_dark"
)

st.plotly_chart(donut, use_container_width=True)

# ----------------------------------
# BUSINESS INSIGHTS
# ----------------------------------

st.subheader("Business Insights")

avg = round(df["Watch_Time"].mean(),2)

st.success(f"Average Watch Time : {avg} Minutes")

drop = round((df["Watch_Time"] < 15).mean()*100,2)

st.error(f"Drop-off Rate : {drop}%")

st.info("""
Recommendations

✔ Reduce Advertisement Duration

✔ Improve Mobile Streaming

✔ Compress Videos

✔ Improve Audio Quality

✔ Personalize Recommendations
""")