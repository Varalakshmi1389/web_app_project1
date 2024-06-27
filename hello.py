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
summary_df = df.groupby(['CreationDate', 'Operation']).agg({'UserId': pd.Series.nunique}).reset_index()
summary_df = summary_df.rename(columns={'UserId': 'Count of Unique Users'})

st.subheader("Summary Table")
st.table(summary_df)


