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
  # Generate summary table
#summary_df = df1.groupby('UserId').size().reset_index(name='Count of Operations')

##st.subheader("Operation Count by Email")
st.table(summary_df)
summary_df = df1.groupby(['UserId', 'CreationDate', 'Operation']).size().reset_index(name='Count of Operations')

st.subheader("Operation Count by Email, CreationDate, and Operation")
st.table(summary_df)


