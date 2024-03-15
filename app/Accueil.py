import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("https://github.com/Badam1666/Elections/blob/main/app/pages/home.py", "Accueil", "🏠"),
        Page("https://github.com/Badam1666/Elections/blob/main/app/pages/page_2.py", "Orientations politiques", "📊"),
        Page("https://github.com/Badam1666/Elections/blob/main/app/pages/page_3.py", "Carte", "🗺️"),
        Page("https://github.com/Badam1666/Elections/blob/main/app/pages/page_4.py", "Commune", "🏘️"),
    ]
)

def main():
    # Hide the current page (app.py) from the sidebar
    st.experimental_set_query_params(page=None)

    st.title("Elections Européennes")
    st.write("Bienvenue sur notre application sur les élections européennes!")

if __name__ == "__main__":
    main()

