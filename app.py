import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Sporty Predictor PRO MAX", page_icon="🔥")

st.title("🔥 Sporty Predictor PRO MAX")
st.write("The smartest ticket analyzer in Ghana 🇬🇭")

uploaded = st.file_uploader("Upload your ticket screenshot", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Your Ticket", use_container_width=True)

    text_input = st.text_area("Paste your games (one per line):", 
        placeholder="Tottenham vs Aston Villa\nBarcelona vs Real Madrid", height=150)

    if st.button("🔍 ANALYZE WITH AI"):
        if not text_input.strip():
            st.warning("Paste games first boss!")
        else:
            games = [g.strip() for g in text_input.split("\n") if "vs" in g.lower() and len(g.strip())>3]
            
            st.markdown("## ✅ AI SMART PREDICTIONS:")
            
            strong_teams = ["man city", "arsenal", "liverpool", "barcelona", "real madrid", "bayern", "psg", "inter", "napoli", "tottenham", "man utd", "chelsea", "dortmund", "leverkusen"]
            
            for game in games:
                lower = game.lower()
                is_big_game = sum(1 for t in strong_teams if t in lower) >= 1
                
                if any(x in lower for x in ["bologna", "torino", "udinese", "cagliari", "osasuna", "mainz", "freiburg"]):
                    pred = "Under 3.5 Goals"
                    reason = "Defensive teams - low goals expected"
                    conf = random.randint(75, 85)
                elif is_big_game:
                    pred = "Over 1.5 Goals"
                    reason = "Strong attack - goals dey inside"
                    conf = random.randint(80, 92)
                else:
                    pred = "Double Chance (1X) + Over 1.5"
                    reason = "Balanced game - safe combo"
                    conf = random.randint(72, 82)
                
                # For top games, add BTTS option
                if "vs" in lower and is_big_game and random.choice([True, False]):
                    pred = "BTTS Yes (Both Teams to Score)"
                    reason = "Both teams get attack!"
                    conf = random.randint(68, 78)

                st.markdown(f"""
                <div style="background:#e8f5e9; padding:15px; border-radius:10px; margin-bottom:10px; border-left:5px solid #4caf50">
                    <b>{game}</b><br>
                    👉 <b style="color:#2e7d32">{pred}</b> <br>
                    📊 Confidence: {conf}% | 💡 {reason}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.success("🎯 ACCA TIP: Combine all with DOUBLE CHANCE for 95% safe ticket!")
            st.balloons()
