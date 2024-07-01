import streamlit as st
import pandas as pd

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

# Initialize page state
page = st.empty()

if "loggedin" not in st.session_state:
    st.session_state.loggedin = False

# Page configuration should be set before any Streamlit elements are created
st.set_page_config(
    page_title="Operations",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Check if logged_in query parameter is set to True
query_params = st.experimental_get_query_params()
if query_params.get('logged_in') == ['true']:
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
            # Redirect to another page after successful login
            st.experimental_set_query_params(logged_in=True)  # Set query params to indicate logged in
            st.experimental_rerun()  # Rerun the script to reflect the new state
    else:
        st.error("Incorrect User ID or Password. Please try again.")
       
