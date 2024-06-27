import streamlit as st
import pandas as pd
import numpy as np

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

# Create a DataFrame
data="‪C:\Users\LAKSHMI\Desktop\Py\inputfile.csv"
df = pd.DataFrame(data)

# Display the DataFrame in Streamlit
st.title("Operation Data")
st.table(df)

