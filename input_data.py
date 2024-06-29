import streamlit as st
import pandas as pd
import plotly.express as px

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

# Set page configuration
st.set_page_config(
    page_title="Operations1",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.sidebar.header("Login")

# Create input fields for User ID and Password
user_id = st.sidebar.text_input("User ID")
password = st.sidebar.text_input("Password", type="password")

# Add a login button
login_button = st.sidebar.button("Login")

# Check credentials upon login button press
if login_button:
    if user_id == CORRECT_USER_ID and password == CORRECT_PASSWORD:
        st.sidebar.success("Logged in successfully!")
        # Place your main application content here
        st.write("Welcome to the application!")
        # Add your main content or other pages here after successful login
    else:
        st.sidebar.error("Incorrect User ID or Password. Please try again.")
