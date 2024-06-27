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

# Create a copy of the DataFrame
df1 = df.copy()

# Convert CreationDate to datetime format and extract date
df1['Date'] = pd.to_datetime(df1['CreationDate']).dt.date

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

# Create for Operation
st.sidebar.header("Choose your filter: ")
operation = st.sidebar.multiselect("Pick your operation", df["Operation"].unique())
if not operation:
    df2 = df.copy()
else:
    df2 = df[df["Operation"].isin(operation)]

# Create for Date
st.sidebar.header("Choose your filter: ")
date = st.sidebar.multiselect("Pick your Date", df["CreationDate"].unique())
if not date:
    df3 = df.copy()
else:
    df3 = df[df["CreationDate"].isin(date)]

# Group by Date to count occurrences of Operation
count_by_date = df1.groupby('Date').size().reset_index(name='Count of Operations')

# Plotting bar chart for Count of Operations by CreationDate
st.subheader("Count of Operations by Creation Date")
fig = px.bar(count_by_date, x='Date', y='Count of Operations', text='Count of Operations',
             template='seaborn', title='Count of Operations by Creation Date')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(xaxis_title='Creation Date', yaxis_title='Count of Operations')
st.plotly_chart(fig, use_container_width=True)
