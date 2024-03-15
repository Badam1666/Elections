import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page(pages.home, "Accueil", "🏠"),
        Page(pages.page_2, "Orientations politiques", "📊"),
        Page(pages.page_3, "Carte", "🗺️"),
        Page(pages.page_4, "Commune", "🏘️"),
    ]
)

def main():
    # Hide the current page (app.py) from the sidebar
    st.experimental_set_query_params(page=None)

    st.title("Elections Européennes")
    st.write("Bienvenue sur notre application sur les élections européennes!")

if __name__ == "__main__":
    main()
