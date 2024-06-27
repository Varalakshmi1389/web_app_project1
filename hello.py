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

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame in Streamlit
    st.subheader("Data Table")
    st.table(df)

    # Generate summary table
    summary_df = df.groupby(['Date', 'Operation', 'Email ID']).size().reset_index(name='Count of Operation')

    st.subheader("Summary Table")
    st.table(summary_df)
else:
    st.write("Please upload a CSV file to see the data.")

