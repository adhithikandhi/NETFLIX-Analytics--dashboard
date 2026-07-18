import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Review Analysis",
    page_icon="😊",
    layout="wide"
)

st.title("😊 User Review & Sentiment Analysis")

st.markdown("---")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

reviews = pd.read_csv("data/reviews.csv")

# -------------------------------------------------
# DATA PREVIEW
# -------------------------------------------------

st.subheader("📋 User Reviews")

st.dataframe(reviews, use_container_width=True)

st.markdown("---")

# -------------------------------------------------
# SENTIMENT ANALYSIS
# -------------------------------------------------

def get_sentiment(text):

    score = TextBlob(str(text)).sentiment.polarity

    if score > 0:
        return "Positive"

    elif score < 0:
        return "Negative"

    else:
        return "Neutral"


reviews["Sentiment"] = reviews["Review"].apply(get_sentiment)

# -------------------------------------------------
# KPI
# -------------------------------------------------

positive = len(reviews[reviews["Sentiment"]=="Positive"])
negative = len(reviews[reviews["Sentiment"]=="Negative"])
neutral = len(reviews[reviews["Sentiment"]=="Neutral"])

c1,c2,c3 = st.columns(3)

c1.metric("😊 Positive", positive)

c2.metric("😐 Neutral", neutral)

c3.metric("😞 Negative", negative)

st.markdown("---")

# -------------------------------------------------
# SENTIMENT PIE CHART
# -------------------------------------------------

fig = px.pie(
    reviews,
    names="Sentiment",
    hole=.60,
    color="Sentiment",
    color_discrete_map={
        "Positive":"green",
        "Neutral":"orange",
        "Negative":"red"
    },
    template="plotly_dark",
    title="Sentiment Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# WORD CLOUD
# -------------------------------------------------

st.subheader("☁️ Word Cloud")

text = " ".join(reviews["Review"].astype(str))

wc = WordCloud(
    width=900,
    height=400,
    background_color="black",
    colormap="Reds"
).generate(text)

fig2,ax = plt.subplots(figsize=(12,5))

ax.imshow(wc)

ax.axis("off")

st.pyplot(fig2)

# -------------------------------------------------
# MOST COMMON WORDS
# -------------------------------------------------

st.subheader("🔥 Most Frequent Words")

words = (
    text.lower()
    .replace(",","")
    .replace(".","")
    .split()
)

freq = pd.Series(words).value_counts().head(15)

freq = freq.reset_index()

freq.columns=["Word","Count"]

bar = px.bar(
    freq,
    x="Word",
    y="Count",
    color="Count",
    template="plotly_dark",
    text="Count",
    title="Top Keywords"
)

st.plotly_chart(bar, use_container_width=True)

# -------------------------------------------------
# REVIEW LENGTH
# -------------------------------------------------

reviews["Length"] = reviews["Review"].str.len()

st.subheader("📝 Review Length")

hist = px.histogram(
    reviews,
    x="Length",
    nbins=10,
    color="Sentiment",
    template="plotly_dark"
)

st.plotly_chart(hist, use_container_width=True)

# -------------------------------------------------
# REVIEW TABLE
# -------------------------------------------------

st.subheader("📑 Review Dataset")

st.dataframe(reviews, use_container_width=True)

# -------------------------------------------------
# BUSINESS INSIGHTS
# -------------------------------------------------

st.subheader("📋 AI Business Insights")

top_issue = freq.iloc[0]["Word"]

st.success(f"Most mentioned keyword: {top_issue}")

if negative > positive:

    st.error("Overall customer satisfaction is low.")

else:

    st.success("Overall customer satisfaction is good.")

st.info("""
### Recommendations

✅ Improve streaming quality

✅ Reduce buffering

✅ Improve audio clarity

✅ Add better subtitles

✅ Optimize advertisements

✅ Improve mobile experience

✅ Recommend content using user behavior
""")