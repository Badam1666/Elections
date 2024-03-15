import streamlit as st

def main():
    # Hide the current page (app.py) from the sidebar
    st.experimental_set_query_params(page=None)

    st.title("Elections Européennes")
    st.write("Bienvenue sur notre application sur les élections européennes!")

if __name__ == "__main__":
    main()
