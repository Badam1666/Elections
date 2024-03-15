import streamlit as st
import time
from datetime import datetime, timedelta

def main():
    st.title("Bienvenue sur le site de Nostradamus")
    st.subheader("Les élections européennes à votre portée")

    # Explication des élections européennes
    st.write("Les prochaines élections européennes auront lieu du 6 au 9 juin 2024. Vous ne savez pas trop comment ces élections fonctionnent et quels sont leurs enjeux ? Pas d'inquiétude, la team Nostradamus vous aide à y voir plus clair !")

    # Description du site
    st.header("Description du site")
    st.write("Sur cette page, vous pouvez trouver les détails de comment nous avons classé les partis politiques en orientations politiques. Sur cette page, vous pouvez trouver une carte des résultats des élections européennes par département de 2004 à 2019. Sur cette page, vous pouvez consulter les résultats de 2014 et 2019 dans votre commune.")

    # Nos prévisions
    st.header("Nos Prévisions")
    st.write("Nous avons utilisé des algorithmes de machine learning pour prévoir les élections 2024. Vous pouvez voir ci-dessous les prévisions de Nostradamus comparées aux sondages Ipsos de début Mars.")

    # Countdown jusqu'au 1er Mai à minuit
    target_datetime = datetime(datetime.now().year, 5, 1, 0, 0)

    countdown_placeholder = st.sidebar.empty()

    while datetime.now() < target_datetime:
        remaining_time = target_datetime - datetime.now()
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_remaining = f"{days} jours, {hours} heures, {minutes} minutes, {seconds} secondes"
        
        countdown_placeholder.markdown("<div style='background-color: #FFD700; padding: 8px; border-radius: 5px;'>"
                                       "<div style='color: black; font-size: small;'>"
                                       f"<p>{time_remaining}</p>"
                                       "</div>"
                                       "</div>", unsafe_allow_html=True)
        
        time.sleep(1)

if __name__ == '__main__':
    main()
