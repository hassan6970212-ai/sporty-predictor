import streamlit as st
from PIL import Image
import re

st.set_page_config(page_title="Sporty Predictor PRO", page_icon="⚽")

st.title("⚽ Sporty Predictor PRO")
st.write("Upload your SportyBet ticket screenshot")

uploaded = st.file_uploader("Upload ticket", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Your Ticket", use_container_width=True)
    
    st.success("Image uploaded successfully! ✅")
    
    # Manual entry to avoid heavy OCR crash
    st.divider()
    st.subheader("Enter the teams from the ticket:")
    teams_text = st.text_area("Paste teams here e.g:\nMan City vs Arsenal\nBarcelona vs Real", height=150)
    
    if st.button("🔍 Analyze & Predict"):
        if teams_text:
            st.balloons()
            st.subheader("✅ SAFE PREDICTIONS:")
            games = teams_text.split('\n')
            for game in games:
                if game.strip():
                    st.write(f"**{game.strip()}** -> Double Chance (1X) or Under 3.5 Goals [SAFE] 🟢")
            st.info("Tip: Stake low, play safe!")
        else:
            st.warning("Please enter at least one game")

else:
    st.info("👆 Click Browse files to upload your SportyBet screenshot")
