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
df1['Count of Operation'] = df1.groupby(['CreationDate', 'Operation', 'UserId'])['UserId'].transform('count')
summary_df = df1.drop_duplicates(subset=['CreationDate', 'Operation', 'UserId'])

st.subheader("Summary Table")
st.table(summary_df[['CreationDate', 'Operation', 'UserId', 'Count of Operation']]


