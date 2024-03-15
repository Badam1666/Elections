import streamlit as st

def main():
    st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
    
    # Customizing the sidebar with the desired name
    st.sidebar.title("Orientations Politiques")
    
    # Your Streamlit app content goes here
    st.write("This is the main content of the page.")

if __name__ == "__main__":
    main()
