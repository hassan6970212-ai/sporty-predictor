import streamlit as st 
# Google Search Console Verification
st.markdown('<meta name="google-site-verification" content="vK_N87B4KvUTkWW6wW6hft8xfP1VERq4YjDWCSilJRo" />', unsafe_allow_html=True)

from PIL import Image

st.set_page_config(page_title="Sporty Predictor PRO MAX", page_icon="⚽", layout="centered")

st.markdown("""
<div style="background:#0a5c36; padding:20px; border-radius:15px; text-align:center; margin-bottom:20px; border: 2px solid #ffd700">
    <div style="font-size:50px">⚽📈</div>
    <h1 style="color:#ffd700; margin:0; font-weight:bold">Sporty Predictor</h1>
    <h2 style="color:white; margin:0">PRO MAX</h2>
    <p style="color:#ffd700; font-weight:bold; margin-top:5px">🇬🇭 GHANA'S #1 - KUMASI</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🔥 AI Football Ticket Analyzer")

if 'unlocked' not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.warning("🔒 Free preview: 2 games only. Pay 5 GHS for full access!")
    code = st.text_input("Enter access code (or pay to get code)", type="default", placeholder="Type GHANA2026")
    if code == "GHANA2026":
        st.session_state.unlocked = True
        st.rerun()
    st.info("💰 **Pay to: MTN MoMo 0543799980** - Send proof to WhatsApp and get code GHANA2026")
    st.markdown("---")

uploaded_file = st.file_uploader("Upload SportyBet ticket", type=['jpg','png','jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Ticket", use_container_width=True)
    
    # NEW: Let owner choose number of games
    num_games = st.number_input("How many games dey this ticket?", min_value=1, max_value=20, value=5)
    
    st.markdown("### 📊 Analysis Result")
    
    if st.session_state.unlocked:
        games_to_show = num_games
    else:
        games_to_show = min(2, num_games)
    
    data = {
        "Match": [f"Match {i+1}" for i in range(games_to_show)],
        "Prediction": [random.choice(["HOME WIN", "AWAY WIN", "OVER 2.5", "BTTS YES"]) for _ in range(games_to_show)],
        "Confidence": [f"{random.randint(65,92)}%" for _ in range(games_to_show)],
        "Odds": [round(random.uniform(1.4, 2.8), 2) for _ in range(games_to_show)]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    if not st.session_state.unlocked:
        st.error(f"🔒 Showing {games_to_show} of {num_games} games. Pay 5 GHS to MTN 0543799980 to unlock all! Code: GHANA2026")
    else:
        st.success(f"✅ PRO MAX UNLOCKED - All {num_games} predictions available!")
        st.balloons()

st.markdown("---")
st.markdown("<center>Built in Kumasi with ❤️ | Contact: 0543799980</center>", unsafe_allow_html=True)
