import streamlit as st
from PIL import Image
import pandas as pd
import random

# PAGE CONFIG
st.set_page_config(page_title="Sporty Predictor PRO MAX", page_icon="⚽", layout="centered")

# LOGO BOX - Professional
st.markdown("""
<div style="background:#0a5c36; padding:20px; border-radius:15px; text-align:center; margin-bottom:20px; border: 2px solid #ffd700">
    <div style="font-size:50px">⚽📈</div>
    <h1 style="color:#ffd700; margin:0; font-weight:bold">Sporty Predictor</h1>
    <h2 style="color:white; margin:0">PRO MAX</h2>
    <p style="color:#ffd700; font-weight:bold; margin-top:5px">🇬🇭 GHANA'S #1 - KUMASI</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🔥 AI Football Ticket Analyzer")

# PAYWALL SYSTEM
if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.warning("🔒 Free preview: 2 games only. Pay 5 GHS for full access!")
    
    code = st.text_input("Enter access code (or pay to get code)", type="password")
    
    col1, col2 = st.columns([1,2])
    with col1:
        if st.button("I have paid - Unlock with code GHANA2026"):
            if code == "GHANA2026" or code == "GHANA2026":
                st.session_state.unlocked = True
                st.success("Unlocked! Reloading...")
                st.rerun()
            else:
                if st.button("Use Code"):
                    pass
    # Direct check
    if code == "GHANA2026":
        st.session_state.unlocked = True
        st.rerun()

    st.info("💰 **Pay to: MTN MoMo 0543799980** - Send proof to WhatsApp and get code GHANA2026")
    
    st.markdown("---")
    st.markdown("**Free Demo:** Upload ticket to see 2 predictions")

# UPLOAD SECTION
uploaded_file = st.file_uploader("Upload SportyBet ticket", type=['jpg','png','jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Ticket", use_container_width=True)
    
    # FAKE ANALYSIS - Demo logic
    st.markdown("### 📊 Analysis Result")
    
    games_to_show = 10 if st.session_state.unlocked else 2
    
    data = {
        "Match": [f"Match {i+1}" for i in range(games_to_show)],
        "Prediction": [random.choice(["HOME WIN", "AWAY WIN", "OVER 2.5", "BTTS YES"]) for _ in range(games_to_show)],
        "Confidence": [f"{random.randint(65,92)}%" for _ in range(games_to_show)],
        "Odds": [round(random.uniform(1.4, 2.8), 2) for _ in range(games_to_show)]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    if not st.session_state.unlocked:
        st.error(f"🔒 Showing {games_to_show} of 10 games. Pay 5 GHS to MTN 0543799980 to unlock all!")
        st.markdown("**WhatsApp proof to 0543799980 and get code GHANA2026**")
    else:
        st.success("✅ PRO MAX UNLOCKED - All predictions available!")
        st.balloons()

st.markdown("---")
st.markdown("<center>Built in Kumasi with ❤️ | Contact: 0543799980</center>", unsafe_allow_html=True)
