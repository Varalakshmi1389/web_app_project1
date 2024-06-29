import streamlit as st
import pandas as pd
import plotly.express as px

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"


# Initialize page state
page = st.sidebar.empty()

if "loggedin" not in st.session_state:
    st.session_state.loggedin = False

if st.session_state.loggedin:
    st.title("Welcome to the Application!")
    # Add your main application content here
    # For example:
    st.write("You are now logged in.")

else:
    st.sidebar.header("Login")

    # Create input fields for User ID and Password
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    # Add a login button
    login_button = st.button("Login")

    # Check credentials upon login button press
    if login_button:
        if user_id == CORRECT_USER_ID and password == CORRECT_PASSWORD:
            st.success("Logged in successfully!")
            st.session_state.loggedin = True
            page.title("Welcome to the Application!")
            # You can redirect or change the main content here after successful login
            st.write("You are now logged in.")
        else:
            st.error("Incorrect User ID or Password. Please try again.")
