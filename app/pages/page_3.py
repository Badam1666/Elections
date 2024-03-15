import streamlit as st
st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)

import streamlit as st
from datetime import datetime, timedelta

def countdown_timer(target_date):
    current_time = datetime.now()
    time_remaining = target_date - current_time
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

def main():
    st.title("Countdown to May 1st, 00:00 AM (UTC+1)")
    target_date = datetime(year=2024, month=5, day=1, hour=0, minute=0, second=0) + timedelta(hours=1)  # Adjusting for UTC+1

    while True:
        days, hours, minutes, seconds = countdown_timer(target_date)
        st.write(f"Time Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        if days == 0 and hours == 0 and minutes == 0 and seconds == 0:
            st.write("Countdown complete!")
            break

if __name__ == "__main__":
    main()
