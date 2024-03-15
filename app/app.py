import streamlit as st
from pages.home import show_home_page
from pages.page_2 import show_page_2
from pages.page_3 import show_page_3
from pages.page_4 import show_page_4

def main():
    # Hide the current page (app.py) from the sidebar
    st.experimental_set_query_params(page=None)

    st.title("Elections Européennes")
    st.write("Bienvenue sur notre application sur les élections européennes!")

if __name__ == "__main__":
    main()
