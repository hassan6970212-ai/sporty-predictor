import streamlit as st
from PIL import Image
import random
import os

st.set_page_config(page_title="Sporty Predictor PRO MAX", page_icon="⚽", layout="centered")

# Pro Ghana colors CSS
st.markdown("""
<style>
.stApp {background: #f8fdf8;}
h1 {color: #0a5c36;}
div[data-testid=\"stFileUploader\"] {border: 2px dashed #0a5c36;}
</style>
""", unsafe_allow_html=True)

# Show logo if exists
if os.path.exists("logo.png"):
    st.image("logo.png", width=250)
else:
    st.title("🔥 Sporty Predictor PRO MAX 🇬🇭")

st.markdown("### Kumasi's #1 AI Football Predictor")
st.write("Upload ticket → Get smart predictions")

# --- PAYWALL ---
if "paid" not in st.session_state:
    st.session_state.paid = False

if not st.session_state.paid:
    st.warning("🔒 Free preview: 2 games only. Pay 5 GHS for full access!")
    access_code = st.text_input("Enter access code (or pay to get code)", type="password")
    if access_code == "GHANA2026" or st.button("I have paid - Unlock with code GHANA2026"):
        if access_code == "GHANA2026":
            st.session_state.paid = True
            st.rerun()
    st.info("💰 Pay to: MTN MoMo 055XXXXXXX - Send proof to WhatsApp and get code GHANA2026")
    limit = 2
else:
    limit = 20
    st.success("✅ PRO MAX Unlocked! Unlimited predictions")

uploaded = st.file_uploader("Upload SportyBet ticket", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, use_container_width=True)
    text_input = st.text_area(f"Paste games (max {limit} games):", height=120)

    if st.button("🔍 PREDICT & WIN"):
        games = [g.strip() for g in text_input.split("\n") if "vs" in g.lower()][:limit]
        if not games:
            st.warning("Paste games!")
        else:
            st.markdown("## ✅ AI PREDICTIONS")
            for game in games:
                low = game.lower()
                if any(x in low for x in ["osasuna","bologna","torino","cagliari","mainz"]):
                    pred, conf, why = "Under 3.5 Goals", random.randint(75,88), "Defensive setup"
                else:
                    pred, conf, why = "Over 1.5 Goals", random.randint(80,92), "Attacking teams"
                st.markdown(f"""
                <div style="background:white; padding:12px; border-radius:10px; margin:6px 0; border-left:5px solid #0a5c36; box-shadow:0 2px 5px #0001">
                <b>{game}</b><br>👉 <b style="color:#0a5c36">{pred}</b> | {conf}% - {why}
                </div>
                """, unsafe_allow_html=True)
            st.balloons()
            st.markdown("---")
            st.markdown("**Share your winning ticket & tag us! 📲**")
