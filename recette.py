import streamlit as st
import pandas as pd
import random
import streamlit.components.v1 as components

# === Chargement des données ===
df = pd.read_csv("recettes.csv")

# === UI avec onglets ===
onglet = st.sidebar.radio("Navigation", ["🎲 Roulette de recettes", "📋 Recos nutrition"])

# === Onglet 1 : Roulette ===
if onglet == "🎲 Roulette de recettes":
    st.title("🎲 Roulette à Recettes")
    st.subheader("Tire une recette au hasard selon le type de repas")

    types_dispo = ["Tous"] + sorted(df["type"].unique())
    choix = st.selectbox("🍽️ Type de repas :", types_dispo)

    # Filtrage
    if choix == "Tous":
        pool = df
    else:
        pool = df[df["type"] == choix]

    # Tirage
    if st.button("🎯 Lancer la roulette"):
        if len(pool) > 0:
            ligne = pool.sample(1).iloc[0]
            st.success(f"👉 {ligne['nom']} ({ligne['type']})")

            pdf_path = f"recettes_pdf/{ligne['pdf']}"

            st.markdown("### 📄 Fiche recette")
            components.html(
                f'<iframe src="{pdf_path}" width="700" height="500"></iframe>',
                height=520,
            )

            # Téléchargement
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Télécharger la fiche PDF",
                    data=f,
                    file_name=ligne['pdf'],
                    mime="application/pdf"
                )
        else:
            st.warning("Aucune recette trouvée pour ce type.")

# === Onglet 2 : Recos nutritionnelles ===
elif onglet == "📋 Recos nutrition":
    st.title("📋 Recommandations nutritionnelles")

    st.markdown("### 🥣 Matin")
    st.markdown("- 1 verre d’eau à jeun avant le café")
    st.markdown("- Bowlcake ou céréales : **20–40 g max** + yaourt")
    st.markdown("- Ou pancakes avec **20–40 g de farine max**")

    st.markdown("### 🥪 Midi")
    st.markdown("- Légumes : 1 bol de soupe ou crudités à volonté")
    st.markdown("- Féculents : **100 g cuits** ou **2 tranches de pain (60 g)** ou **1 wrap**")
    st.markdown("- Protéines : charcuterie maigre, poisson, œufs, légumineuses (au moins **100 g**) ou à tartiner")
    st.markdown("- Fromage : **30–40 g**")
    st.markdown("- Sauce/huile allégée pour napper ou tartiner")

    st.markdown("### 🍏 Collation")
    st.markdown("- 1 fruit **et** 1 laitage")

    st.markdown("### 🍽️ Soir")
    st.markdown("- Féculents : **100–150 g cuits**")
    st.markdown("- Protéines : **150 g** de viande/alternative")
    st.markdown("- Légumes : ½ assiette (⚠️ salade seule = pas assez)")
    st.markdown("- Sauce/huile allégée en quantité raisonnable")

    st.markdown("### 💤 Collation (si faim)")
    st.markdown("- 1 fruit **ou** 1 laitage")

    st.caption("👩‍⚕️ Perrine Errard – Diététicienne-Nutritionniste Agréée")

