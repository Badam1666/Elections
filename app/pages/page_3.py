import streamlit as st
st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)



def show_page_3():
    st.title("Carte")
    st.write("Contenu de la page 3")
    # Add more content or Streamlit components as needed for page 3

import time
from datetime import datetime, timezone, timedelta

def count_down(ts):
    with st.empty():
        while ts:
            current_time = datetime.now(timezone.utc) + timedelta(hours=1)  # UTC+1 time
            if current_time >= datetime(2024, 5, 1, 0, 0, tzinfo=timezone.utc):
                st.header("Fin des inscriptions en ligne")
                break
            
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1
        else:
            st.header("Time Up!")

def main():
    st.title("Countdown Timer")
    time_minutes = st.number_input('Enter the time in minutes ', min_value=1, value=25)
    time_in_seconds = time_minutes * 60
    
    if st.button("START"):
        count_down(int(time_in_seconds))

if __name__ == '__main__':
    main()
