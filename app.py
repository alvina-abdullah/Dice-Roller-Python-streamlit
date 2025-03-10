import random
import streamlit as st
import time

def roll_dice():
    return random.randint(1, 6)

def main():
    st.set_page_config(page_title="Dice Roller", page_icon="🎲", layout="centered")
    
    st.sidebar.title("🎲 Dice Roller Game")
 
    
    st.sidebar.markdown("## How to Play:")
    st.sidebar.write("- Each player gets one chance to roll.")
    st.sidebar.write("- If a player rolls a 6, they win instantly!")
    st.sidebar.write("- If no one rolls a 6, try again!")
    
    st.markdown("""
        <style>
            body { background-color: #121212; color: white; }
            .stButton>button {
                background-color: white;
                color: black;
                font-size: 18px;
                padding: 12px;
                border-radius: 10px;
                transition: 0.3s;
            }
            .stButton>button:hover {
                transform: scale(1.05);
                cursor: pointer;
            }
            .dice-face {
                text-align: center;
                font-size: 150px;
                margin: 20px 0;
            }
            .winner {
                color: #FFD700;
                font-size: 24px;
                font-weight: bold;
            }
        """, unsafe_allow_html=True)
    
    st.title("**🎲 Ultimate Dice Roller – Roll & Test Your Luck! 🎲**")
    st.write("**Each player gets one chance to roll. If a player rolls a 6, they win instantly!**")
    
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }
    
    if "scores" not in st.session_state:
        st.session_state.scores = {"Player 1": None, "Player 2": None, "Player 3": None, "Player 4": None}
    
    winner = None
    all_rolled = True
    
    for player in st.session_state.scores.keys():
        if st.session_state.scores[player] is None:
            all_rolled = False
            if st.button(f"🎲 {player} Roll The Dice 🎲"):
                with st.spinner("Rolling..."):
                    time.sleep(1.5)
                
                dice_value = roll_dice()
                st.session_state.scores[player] = dice_value
                
                st.subheader(f"{player} rolled: {dice_value}")
                st.markdown(f"<div class='dice-face'>{dice_faces[dice_value]}</div>", unsafe_allow_html=True)
                
                if dice_value == 6:
                    winner = player
                    break
    
    if winner:
        st.success(f"🎉 {winner} rolled a 6 and WINS the game!")
        st.markdown(f"<div class='winner'>🏆 Congratulations {winner}! 🏆</div>", unsafe_allow_html=True)
        st.session_state.scores = {"Player 1": None, "Player 2": None, "Player 3": None, "Player 4": None}  # Reset scores after a win
        st.balloons()
    elif all_rolled:
        st.warning("😢 No one rolled a 6! Try again!")
        if st.button("🔄 Try Again"):
            st.session_state.scores = {"Player 1": None, "Player 2": None, "Player 3": None, "Player 4": None}
            st.rerun()
    
    st.markdown("## 🏆 Scoreboard 🏆")
    for player, score in st.session_state.scores.items():
        st.write(f"**{player}:** {score if score is not None else 'Not rolled yet'}")
    
    st.markdown("---")
    st.markdown(" **© 2025 Alvina Abdullah. Built with 🩷. \n All rights Reserved** ")
   
if __name__ == "__main__":
    main()
