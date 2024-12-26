import streamlit as st
from authentication import login, otp_verification
from document_processing import dashboard
from css import apply_custom_css

st.set_page_config(page_title="Dynamo.ai", layout="wide")

# Apply custom CSS styling
apply_custom_css()

def main():
    if 'stage' not in st.session_state:
        st.session_state.stage = "login"

    if st.session_state.stage == "login":
        login()
    elif st.session_state.stage == "otp_verification":
        otp_verification()
    elif st.session_state.logged_in:
        dashboard()

if __name__ == "__main__":
    main()
