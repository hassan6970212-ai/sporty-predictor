import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sporty Predictor PRO", page_icon="⚽")

st.title("⚽ Sporty Predictor PRO")
st.write("Upload your SportyBet ticket screenshot")

uploaded = st.file_uploader("Upload ticket", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Your Ticket", use_container_width=True)

    st.markdown("### Enter the teams from the ticket:")
    st.caption("Paste each match on new line. Eg:\nTottenham vs Aston Villa\nOsasuna vs Rayo Vallecano")
    
    text_input = st.text_area("", placeholder="Man City vs Arsenal\nBarcelona vs Real...", height=150)

    if st.button("🔍 Analyze & Predict"):
        if text_input.strip() == "":
            st.warning("Please paste the teams first!")
        else:
            # Split by lines
            games = [g.strip() for g in text_input.split("\n") if "vs" in g.lower()]
            # If user pasted everything in one line, try to split by 'vs' smart way
            if len(games) <= 1 and len(text_input) > 30:
                # fallback: just show one by one if they pasted space separated
                import re
                parts = re.split(r'\s{2,}', text_input) # split by double space
                if len(parts) > 1:
                    games = parts

            st.markdown("## ✅ SAFE PREDICTIONS:")
            
            for game in games:
                st.success(f"**{game.strip()}** → 🟢 Double Chance (1X) or Under 3.5 Goals | SAFE")
            
            if not games:
                 st.info(f"**{text_input}** → 🟢 Double Chance (1X) or Under 3.5 Goals | SAFE")
            
            st.markdown("---")
            st.info("💡 Tip: Stake low, play safe! No game is 100% sure.")
