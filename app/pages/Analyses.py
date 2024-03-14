import streamlit as st
from streamlit.components.v1 import components_v1

def main():
    st.title("Rickroll without Ads 🎵")

    # YouTube video ID for the Rickroll video
    video_id = "dQw4w9WgXcQ"

    # Constructing the URL for the embedded video
    youtube_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1"

    # HTML code for embedding the YouTube video
    html_code = f"""
    <iframe width="560" height="315" src="{youtube_url}" frameborder="0" allowfullscreen></iframe>
    """

    # Displaying the embedded video
    components_v1.html(html_code, width=700, height=400)

if __name__ == "__main__":
    main()

