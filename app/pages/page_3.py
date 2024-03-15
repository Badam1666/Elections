import streamlit as st
st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)




import time
from datetime import datetime, timezone, timedelta

def count_down(target_datetime):
    with st.empty():
        while datetime.now(timezone.utc) < target_datetime:
            remaining_time = target_datetime - datetime.now(timezone.utc)
            days, seconds = divmod(remaining_time.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            
            time_remaining = f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
            
            st.header(f"{time_remaining}")
            time.sleep(1)
        
        st.header("Fin des inscriptions en ligne")

def main():
    st.title("Countdown to May 1st, 2024")
    target_datetime = datetime(2024, 5, 1, 0, 0, tzinfo=timezone.utc)
    
    count_down(target_datetime)

if __name__ == '__main__':
    main()
