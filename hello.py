import streamlit as st
import pandas as pd

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

st.title("Operation Data")
df1=df.copy()

df1['date'] = pd.to_datetime(df1['CreationDate']).dt.date

    # Group by UserId, CreationDate, and Operation to count occurrences
summary_df = df1.groupby(['UserId', 'date', 'Operation']).size().reset_index(name='Count of Operations')

    # Aggregate the count of operations by UserId
final_summary_df = summary_df.groupby('UserId').agg({
    'CreationDate': 'first',  # Assuming CreationDate is consistent per UserId
    'Operation': 'first',     # Assuming Operation is consistent per UserId
    'Count of Operations': 'sum'
}).reset_index()

st.subheader("Operation Count by Email, CreationDate, and Operation")
st.table(final_summary_df[['UserId', 'CreationDate', 'Operation', 'Count of Operations']])





