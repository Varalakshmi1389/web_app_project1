import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
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

# Load data
df = pd.read_csv("inputfile.csv")
st.write(df)

# Convert CreationDate to datetime format and extract date
df['Date'] = pd.to_datetime(df['CreationDate']).dt.date

# Create a copy of the DataFrame
df1 = df.copy()

# Group by UserId, Date, and Operation to count occurrences
summary_df = df1.groupby(['UserId', 'Date', 'Operation']).size().reset_index(name='Count of Operations')

# Aggregate the count of operations by UserId
final_summary_df = summary_df.groupby('UserId').agg({
    'Date': 'first',
    'Operation': 'first',
    'Count of Operations': 'sum'
}).reset_index()

st.subheader("Operation Count by UserId, Date, and Operation")
st.table(final_summary_df[['UserId', 'Date', 'Operation', 'Count of Operations']])

# Sidebar filters for Operation and CreationDate
st.sidebar.header("Filters")
selected_operation = st.sidebar.multiselect("Select Operation(s)", df["Operation"].unique())
selected_dates
