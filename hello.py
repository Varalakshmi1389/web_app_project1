import streamlit as st

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

# Initialize page state
page = st.empty()

if "loggedin" not in st.session_state:
    st.session_state.loggedin = False

if st.session_state.loggedin:
    st.title("Welcome to the Application!")
    # Add your main application content here
    # For example:
    st.write("You are now logged in.")

    # Redirect to another page after successful login
    st.experimental_set_query_params(logged_in=True)  # Set query params to indicate logged in

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
            # You can redirect or change the main content here after successful login
            st.write("You are now logged in.")

            # Redirect to another page after successful login
            st.experimental_set_query_params(logged_in=True)  # Set query params to indicate logged in
        else:
            st.error("Incorrect User ID or Password. Please try again.")

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

# Check if logged_in query parameter is set to True, then navigate to another page
if st.experimental_get_query_params().get('logged_in'):
    st.write("Redirecting to another page...")
    # Replace with code to navigate to another Streamlit page or load another content
    # For demonstration, you can simulate navigation using st.write or st.markdown
    st.write("You have successfully logged in!")
