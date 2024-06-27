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

# Read data from CSV file
csv_file_path = "C:/Users/LAKSHMI/Desktop/Py/inputfile.csv"
df = pd.read_csv(csv_file_path)

# Display the DataFrame in Streamlit
st.title("Operation Data")
st.table(df)
