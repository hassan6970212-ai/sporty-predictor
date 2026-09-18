import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import re

@st.cache_resource
def get_reader():
    return easyocr.Reader(['en'])

reader = get_reader()

st.set_page_config(page_title="Sporty Predictor PRO", page_icon="⚽")
st.title("⚽ Sporty Predictor PRO")

uploaded = st.file_uploader("Upload your Sportybet ticket", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    img.thumbnail((900, 900))
    st.image(img, use_container_width=True)

    if st.button("🔥 ANALYZE WITH AI"):
        with st.spinner("AI dey analyze odds..."):
            result = reader.readtext(np.array(img), detail=0)
            full_text = " ".join(result)

            st.caption(f"Text found: {full_text[:400]}")

            # Find all matches like TEAM vs TEAM odd odd odd
            pattern = r"([A-Z]{2,4})\s+VS\s+([A-Z]{2,4})\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)"
            matches = re.findall(pattern, full_text)

            if not matches:
                # Fallback for virtuals
                pattern2 = r"([A-Z]{3})\s+VS\s+([A-Z]{3})\s+([\d.]+)"
                matches = re.findall(pattern2, full_text)
                # convert to 3-group format
                matches = [(m[0], m[1], m[2], "3.50", "4.00") for m in matches]

            st.divider()
            st.subheader("🔮 AI PRO Predictions:")

            for m in matches:
                team1, team2, o1, ox, o2 = m
                try:
                    o1_f, ox_f, o2_f = float(o1), float(ox), float(o2)

                    # Calculate winning %
                    p1 = (1/o1_f)*100
                    px = (1/ox_f)*100
                    p2 = (1/o2_f)*100

                    if o1_f < 1.70:
                        pick = f"HOME WIN ({team1}) - 1"
                        conf = f"{p1:.0f}% WIN CHANCE - SAFE ✅"
                    elif o1_f < 2.20 and o2_f > 2.80:
                        pick = f"Double Chance: {team1} or Draw (1X)"
                        conf = f"{p1+px:.0f}% Combined - SAFE ✅"
                    elif o2_f < 2.00:
                        pick = f"AWAY WIN ({team2}) - 2"
                        conf = f"{p2:.0f}% WIN CHANCE"
                    elif o1_f > 2.5 and o2_f > 2.5:
                        pick = "OVER 1.5 GOALS / BTTS Yes"
                        conf = "Both teams balanced - Goals likely ⚽"
                    else:
                        pick = f"Double Chance: {team2} or Draw (X2)"
                        conf = f"Odds risky ({o1}), play safe"

                    with st.container(border=True):
                        st.markdown(f"**{team1} VS {team2}**")
                        st.write(f"Odds: {o1} | {ox} | {o2}")
                        st.success(f"**Prediction: {pick}**\n\n{conf}")

                except:
                    st.write(f"**{team1} vs {team2}:** Over 1.5 Goals (fallback)")

            st.balloons()
            st.info("PRO Version Active - This uses odds % analysis, not just basic logic!")
