import random
import streamlit as st
import time

def roll_dice():
    return random.randint(1, 6)

def main():
    st.set_page_config(page_title="Dice Roller", page_icon="🎲", layout="centered")
    
    st.markdown("""
        <style>
            body { background-color: #1E1E1E; color: white; }
            .stButton>button {
                background-color: #FF5733;
                color: white;
                font-size: 22px;
                padding: 12px;
                border-radius: 10px;
                transition: 0.3s;
                
            }
            .stButton>button:hover {
                background-color: #C70039;
                transform: scale(1.05);
                cursor: pointer;
            }
            .dice-face {
                text-align: center;
                font-size: 150px;
                margin: 20px 0;
            }
        """, unsafe_allow_html=True)
    
    st.title("**🎲 Ultimate Dice Roller – Roll & Test Your Luck! 🎲**")
    st.write("**Press the magic button below to roll the dice and test your luck!✨**")
    
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }
    
    if st.button("🔥 Roll The Dice 🔥"):
        with st.spinner("Rolling..."):
            time.sleep(1.5)
        
        dice_value = roll_dice()
        st.subheader(f"You rolled: {dice_value}")
        st.markdown(f"<div class='dice-face'>{dice_faces[dice_value]}</div>", unsafe_allow_html=True)
        
        if dice_value == 6:
            st.success("🎉 Jackpot! You hit the highest number!")
        elif dice_value == 1:
            st.error("😢 Oh no! You got the lowest number. Try again!")
        else:
            st.info("🎲 Not bad! Give it another shot!")
        
        st.balloons()
    
    st.markdown("---")
    st.markdown(" **© 2025 Alvina Abdullah. Built with 🩷. \n All rights Reserved** \t | 🎨 Designed for Fun!  ")
   
    
if __name__ == "__main__":
    main()
