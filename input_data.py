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
selected_dates = st.sidebar.multiselect("Select Date(s)", df["CreationDate"].unique())

# Apply filters to create filtered DataFrame
if selected_operation:
    df = df[df['Operation'].isin(selected_operation)]
if selected_dates:
    df = df[df['CreationDate'].isin(selected_dates)]

# Group by Date to count occurrences of Operation
count_by_date = df.groupby('Date').size().reset_index(name='Count of Operations')

# Plotting bar chart for Count of Operations by CreationDate
st.subheader("Count of Operations by Creation Date")
fig_bar = px.bar(count_by_date, x='Date', y='Count of Operations', text='Count of Operations',
                 template='seaborn', title='Count of Operations by Creation Date')
fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_bar.update_layout(xaxis_title='Creation Date', yaxis_title='Count of Operations')
st.plotly_chart(fig_bar, use_container_width=True)

# Group by Operation to sum RecordType
record_type_summary = df.groupby('Operation')['RecordType'].sum().reset_index()

# Plotting pie chart for Sum of RecordType by Operation
st.subheader("Sum of RecordType by Operation")
fig_pie = px.pie(record_type_summary, values='RecordType', names='Operation', 
                 title='Sum of RecordType by Operation', hole=0.5)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)

