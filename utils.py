import streamlit as st

def page_title(title):

    st.markdown(
        f"""
        <h1 style='color:#E50914;
        text-align:center;'>
        {title}
        </h1>
        """,
        unsafe_allow_html=True
    )


def section_title(title):

    st.markdown(
        f"""
        <h3 style='color:white'>
        {title}
        </h3>
        """,
        unsafe_allow_html=True
    )


def horizontal():

    st.markdown("---")