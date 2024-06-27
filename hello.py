import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

df=pd.read_csv("inputfile.csv")
st.write(df)

df1=df.copy()

df1['Date'] = pd.to_datetime(df1['CreationDate']).dt.date
#Creating table with count of operations based userid,date and opeartion
summary_df = df1.groupby(['UserId', 'Date', 'Operation']).size().reset_index(name='Count of Operations')

final_summary_df = summary_df.groupby('UserId').agg({
    'Date': 'first', 
    'Operation': 'first',
    'Count of Operations': 'sum'
}).reset_index()
st.subheader("Operation Count by UserId, Date, and Operation")
st.table(final_summary_df[['UserId', 'Date', 'Operation', 'Count of Operations']])

record_type_summary = df1.groupby('Operation')['RecordType'].sum().reset_index()

# Plotting pie chart for sum of RecordType by Operation
fig, ax = plt.subplots()
ax.pie(record_type_summary['RecordType'], labels=record_type_summary['Operation'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.subheader("Pie Chart: Sum of RecordType by Operation")
st.pyplot(fig)




