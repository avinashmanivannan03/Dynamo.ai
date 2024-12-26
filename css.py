import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .main {
            background-color: #f0f0f5;
            color: #4c4c8a;
        }
        .stButton>button {
            background-color: #4c4c8a;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #4c4c8a;
            padding: 10px;
        }
        .stSidebar {
            background-color: #333366;
            color: white;
        }
        .stSidebar button {
            background-color: #4c4c8a;
            color: white;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)
