import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

# Page configuration should be set before any Streamlit elements are created
st.set_page_config(
    page_title="Operations",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# Function to display the main content after login
def display_main_content(df_merged):
    st.subheader("Operation Count by UserId, Date, and Operation")

    # Sidebar filters for Operation and CreationDate
    st.sidebar.header("Filters")
    selected_operation = st.sidebar.multiselect("Select Operation(s)", df_merged["Operation"].unique())
    selected_dates = st.sidebar.multiselect("Select Date(s)", df_merged["CreationDate"].unique())

    # Apply filters to create filtered DataFrame
    if selected_operation:
        df_filtered = df_merged[df_merged['Operation'].isin(selected_operation)]
    else:
        df_filtered = df_merged.copy()
    if selected_dates:
        df_filtered = df_filtered[df_filtered['CreationDate'].isin(selected_dates)]

    # Group by UserId, Date, and Operation to count occurrences
    summary_df = df_filtered.groupby(['Fullname', 'UserId', 'CreationDate', 'Operation']).size().reset_index(name='Count of Operations')

    final_summary_df = summary_df.groupby('Fullname').agg({
        'UserId': 'first',
        'CreationDate': 'first',
        'Operation': 'first',
        'Count of Operations': 'sum'
    }).reset_index()

    st.table(final_summary_df[['Fullname', 'UserId', 'CreationDate', 'Operation', 'Count of Operations']])

    # Group by Date to count occurrences of Operation
    count_by_date = df_filtered.groupby('CreationDate').size().reset_index(name='Count of Operations')

    # Plotting bar chart for Count of Operations by CreationDate
    st.subheader("Count of Operations by Creation Date")
    fig_bar = px.bar(count_by_date, x='CreationDate', y='Count of Operations', text='Count of Operations',
                     template='seaborn', title='Count of Operations by Creation Date')
    fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig_bar.update_layout(xaxis_title='Creation Date', yaxis_title='Count of Operations')
    st.plotly_chart(fig_bar, use_container_width=True)

    # Group by Operation to sum RecordType
    record_type_summary = df_filtered.groupby('Operation')['RecordType'].sum().reset_index()

    # Plotting pie chart for Sum of RecordType by Operation
    st.subheader("Sum of RecordType by Operation")
    fig_pie = px.pie(record_type_summary, values='RecordType', names='Operation',
                     title='Sum of RecordType by Operation', hole=0.5)
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)


# Function to display another page content
def display_another_page(df_merged):
    st.title("Page 
