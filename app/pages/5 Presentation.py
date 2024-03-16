import streamlit as st
st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)
# Title
st.title("Présentation du 15 Mars 2024")

# Embed Google Slides presentation using an <iframe> tag
st.markdown(
    """
    <iframe src="https://docs.google.com/presentation/d/1zKvvjRn7vbbdqqKRBzoQ6MjihuqhPbQgAGjBSxsGNc0/embed?start=false&loop=false&delayms=3000" 
    width="100%" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    """,
    unsafe_allow_html=True
)
