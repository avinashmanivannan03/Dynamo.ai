import streamlit as st
import json
import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_login_data():
    if os.path.exists("login_data.json"):
        with open("login_data.json", "r") as file:
            return json.load(file)
    return {"login": []}  


def save_login_data(data):
    with open("login_data.json", "w") as file:
        json.dump(data, file, indent=4)


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(sender_email, sender_password, recipient_email, otp):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Your OTP Code"

    body = f"Your OTP code is: {otp}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        st.success(f"OTP sent to {recipient_email}")
    except Exception as e:
        st.error(f"Failed to send OTP. Error: {str(e)}")


def login():
    st.title("🔑 Login or Create Account")
    
    
    tabs = st.tabs(["Login", "Create Account"])
    
    with tabs[0]:
        st.markdown("### Please enter your credentials")
        username = st.text_input("📧 Email")
        password = st.text_input("🔒 Password", type="password")

        if st.button("Login"):
            data = load_login_data()
            if data is None:
                st.error("Error: Failed to load login data.")
                return

            if 'login' not in data:
                st.error("Error: 'login' key not found in the data.")
                return

            user_found = False
            for user in data['login']:
                if username == user['email'] and password == user['password']:
                    user_found = True
                    st.session_state.username = username
                    st.session_state.role = user['role']
                    st.session_state.otp = generate_otp()
                    send_otp_email("teamaraycci@gmail.com", "popb atyu fjhw dtqu", username, st.session_state.otp)
                    st.session_state.stage = "otp_verification"
                    
                    
                    if f'chat_history_{username}' not in st.session_state:
                        st.session_state[f'chat_history_{username}'] = []
                    st.rerun()
                    break
            if not user_found:
                st.error("Invalid username or password")

    with tabs[1]:
        st.markdown("### Create a New Account")
        new_username = st.text_input("New Email", key="new_email")
        new_password = st.text_input("New Password", type="password", key="new_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

        if st.button("Create Account"):
            if new_password != confirm_password:
                st.error("Passwords do not match!")
            else:
                data = load_login_data()
                user_exists = any(user['email'] == new_username for user in data['login'])
                if user_exists:
                    st.error("User already exists!")
                else:
                    new_user = {
                        "email": new_username,
                        "password": new_password,
                        "role": "user" 
                    }
                    data['login'].append(new_user)
                    save_login_data(data)
                    st.success("Account created successfully! You can now log in.")


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


def main():
    if 'stage' not in st.session_state:
        st.session_state.stage = "login"

    if st.session_state.stage == "login":
        login()
    elif st.session_state.stage == "otp_verification":
        otp_verification()
    elif st.session_state.stage == "dashboard":
        st.title("Welcome to the Dashboard!")
        st.write("You are logged in as:", st.session_state.username)

if __name__ == "__main__":
    main()
