import streamlit as st
import smtplib
import random
import string
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from document_processing import generate_otp, send_otp_email
from utils import load_login_data


def login():
    st.title("🔑 Login")
    st.markdown("### Please enter your credentials")
    username = st.text_input("📧 Email")
    password = st.text_input("🔒 Password", type="password")
    
    if st.button("Login"):
        data = load_login_data()
        if data is None:
            print("Error: Failed to load login data.")
            return
        
        if 'login' not in data:
            print("Error: 'login' key not found in the data.")
            return
        
        for user in data['login']:
            if username == user['email'] and password == user['password']:
                user_found = True
                st.session_state.username = username
                st.session_state.role = user['role']
                st.session_state.otp = generate_otp()
                send_otp_email("teamaraycci@gmail.com", "popb atyu fjhw dtqu", username, st.session_state.otp)
                st.session_state.stage = "otp_verification"
                
                # Initialize user-specific chat history if it doesn't exist
                if f'chat_history_{username}' not in st.session_state:
                    st.session_state[f'chat_history_{username}'] = []
                st.rerun()
                break
        if not user_found:
            st.error("Invalid username or password")

def otp_verification():
    st.title("🔐 OTP Verification")
    st.markdown("### Please enter the OTP sent to your email")
    user_input = st.text_input("Enter OTP:")
    
    if st.button("Verify"):
        if user_input == st.session_state.otp:
            st.session_state.logged_in = True
            st.session_state.stage = "dashboard"
            st.success("✅ OTP Verified Successfully")
            st.rerun()
        else:
            st.error("❌ Invalid OTP. Please try again.")
