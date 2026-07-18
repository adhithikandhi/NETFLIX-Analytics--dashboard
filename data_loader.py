import pandas as pd
import streamlit as st
from config import *

@st.cache_data
def load_watch_data():
    return pd.read_csv(WATCH_DATA)

@st.cache_data
def load_users():
    return pd.read_csv(USERS_DATA)

@st.cache_data
def load_reviews():
    return pd.read_csv(REVIEWS_DATA)

@st.cache_data
def load_network():
    return pd.read_csv(NETWORK_DATA)

@st.cache_data
def load_ads():
    return pd.read_csv(ADS_DATA)