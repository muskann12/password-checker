import re
import random
import streamlit as st

# Define special characters for password generation
SPECIAL_CHARACTERS = "!@#$%^&*"

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(f"[{SPECIAL_CHARACTERS}]", password):
        score += 1
    else:
        feedback.append(f"❌ Include at least one special character ({SPECIAL_CHARACTERS}).")

    return score, feedback

# Function to generate a strong password
def generate_strong_password():
    password_length = 12
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    digits = "0123456789"
    all_chars = lower + upper + digits + SPECIAL_CHARACTERS
    return "".join(random.sample(all_chars, password_length))

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter By Muskan Nisar", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Check your password's strength & improve security! 🔥</p>", unsafe_allow_html=True)

# User input for password
password = st.text_input("Enter your password:", type="password")

# Check password strength button
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Password Strength Indicator
        if score == 4:
            st.success("✅ Strong Password! 💪")
            st.progress(1.0)  # Full bar for strong password
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            st.progress(0.75)
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
            st.progress(0.4)

        # Show feedback
        if feedback:
            st.subheader("🔎 Suggestions:")
            for f in feedback:
                st.write(f)
    else:
        st.error("⚠️ Please enter a password!")

# Password Generator
st.markdown("---")
st.subheader("🔑 Need a Strong Password?")
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text_input("Your Strong Password:", strong_password, disabled=True)
