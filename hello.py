import streamlit as st
import pandas as pd
import plotly.express as px

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

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

# Function to display the main content after login
def display_main_content():
    # Load the primary CSV file
    try:
        df = pd.read_csv("inputfile.csv")
    except FileNotFoundError:
        st.error("The file 'inputfile.csv' was not found.")
        return

    # Load the secondary CSV file and perform a left join
    try:
        df1 = pd.read_csv("inputfile1.csv")
        df_merged = pd.merge(df, df1, left_on='UserId', right_on='Userid', how='left')
    except FileNotFoundError:
        st.warning("The file 'inputfile1.csv' was not found. Proceeding with only 'inputfile.csv'.")
        df_merged = df

    st.write(df_merged)

    df_merged['Date'] = pd.to_datetime(df_merged['CreationDate']).dt.date
    df1_copy = df_merged.copy()

    # Group by UserId, Date, and Operation to count occurrences
    summary_df = df1_copy.groupby(['UserId', 'Date', 'Operation']).size().reset_index(name='Count of Operations')

    final_summary_df = summary_df.groupby('UserId').agg({
        'Date': 'first',
        'Operation': 'first',
        'Count of Operations': 'sum'
    }).reset_index()

    st.subheader("Operation Count by UserId, Date, and Operation")
    st.table(final_summary_df[['UserId', 'Date', 'Operation', 'Count of Operations']])

    # Sidebar filters for Operation and CreationDate
    st.sidebar.header("Filters")
    selected_operation = st.sidebar.multiselect("Select Operation(s)", df_merged["Operation"].unique())
    selected_dates = st.sidebar.multiselect("Select Date(s)", df_merged["CreationDate"].unique())

    # Apply filters to create filtered DataFrame
    if selected_operation:
        df_merged = df_merged[df_merged['Operation'].isin(selected_operation)]
    if selected_dates:
        df_merged = df_merged[df_merged['CreationDate'].isin(selected_dates)]

    # Group by Date to count occurrences of Operation
    count_by_date = df_merged.groupby('Date').size().reset_index(name='Count of Operations')

    # Plotting bar chart for Count of Operations by CreationDate
    st.subheader("Count of Operations by Creation Date")
    fig_bar = px.bar(count_by_date, x='Date', y='Count of Operations', text='Count of Operations',
                     template='seaborn', title='Count of Operations by Creation Date')
    fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig_bar.update_layout(xaxis_title='Creation Date', yaxis_title='Count of Operations')
    st.plotly_chart(fig_bar, use_container_width=True)

    # Group by Operation to sum RecordType
    record_type_summary = df_merged.groupby('Operation')['RecordType'].sum().reset_index()

    # Plotting pie chart for Sum of RecordType by Operation
    st.subheader("Sum of RecordType by Operation")
    fig_pie = px.pie(record_type_summary, values='RecordType', names='Operation', 
                     title='Sum of RecordType by Operation', hole=0.5)
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

# Function to display another page content
def display_another_page():
    st.title("Page2")
    st.write("This is another page content.")
    # Add more content for the new page as needed

# Initialize page state
if "loggedin" not in st.session_state:
    st.session_state.loggedin = False

# Check if logged_in query parameter is set to True
query_params = st.experimental_get_query_params()
if query_params.get('logged_in') == ['true']:
    st.session_state.loggedin = True

# Check if logged in and display content accordingly
if st.session_state.loggedin:
    # Navigation links in the sidebar
    st.sidebar.header("Navigation")
    if st.sidebar.button("Page1"):
        st.experimental_set_query_params(logged_in=True, page="main")
        st.experimental_rerun()
    if st.sidebar.button("Page2"):
        st.experimental_set_query_params(logged_in=True, page="another")
        st.experimental_rerun()

    if query_params.get('page', ['main'])[0] == 'main':
        display_main_content()
    elif query_params.get('page', ['main'])[0] == 'another':
        display_another_page()
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
