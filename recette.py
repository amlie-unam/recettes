import streamlit as st
import pandas as pd
import random

# Charger les recettes
df = pd.read_csv("recettes.csv")

st.title("🎲 Roulette à Recettes")
st.subheader("Choisis un type de repas et tire une recette au hasard !")

# Filtrer par type
types_dispo = ["Tous"] + sorted(df["type"].unique())
choix = st.selectbox("🍽️ Type de repas :", types_dispo)

# Appliquer le filtre
if choix == "Tous":
    pool = df
else:
    pool = df[df["type"] == choix]

# Tirage
if st.button("🎯 Lancer la roulette"):
    if len(pool) > 0:
        recette = random.choice(pool["nom"].tolist())
        st.success(f"👉 {recette}")
    else:
        st.warning("Aucune recette trouvée pour ce type.")
