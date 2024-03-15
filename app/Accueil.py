import streamlit as st
st.set_page_config(page_title="Elections européennes", page_icon="🗳️", layout="centered", initial_sidebar_state="auto", menu_items=None)


def main():
    st.title("Projet Nostradamus : Analyse des dernières élections européennes et prédiction pour 2024 🔮")
    st.write("Les élections européennes sont l’occasion pour les citoyens de participer activement à la vie démocratique de l’Union européenne et d’influencer les décisions qui impactent leur quotidien. Alors, allons voter !")
    st.write("Allez vérifier votre inscription sur ce lien : [Lien vers le service-public.fr](https://www.service-public.fr/particuliers/vosdroits/demarches-et-outils/ISE)")

    st.header("Projet de 2 semaines dans le cadre de la formation du Wagon en data analytics")
    st.write("Comprendre les élections européennes et leurs enjeux")
    st.write("Contexte électoral français")
    st.write("Décryptage des votes : Comprendre les tendances électorales")
    st.write("Étude de cas : Focus sur la Haute Garonne")
    st.write("Prédictions pour les élections européennes de 2024")

    st.write("N’oublions pas que ces prédictions sont basées sur des tendances actuelles et peuvent évoluer. Restons attentifs aux développements politiques et aux changements sociodémographiques pour affiner nos prévisions.")

if __name__ == "__main__":
    main()

if st.button("Carte"):
    st.switch_page("pages/page_2.py")
