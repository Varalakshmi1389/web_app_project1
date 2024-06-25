import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title(":bar_chart: Sales Dashboard")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    st.write(df)
else:
    df=pd.read_csv("salesdatacsvsample.csv")
    st.write(df)

col1, col2 = st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()
with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()
st.sidebar.header("Select your filter: ")
state = st.sidebar.multiselect("Select the State", df2["State"].unique())
df2=df.copy()
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]
    
