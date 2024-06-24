import streamlit as st
import pandas as pd
import numpy as np
st.write("My name is varalakshmi")
st.write("Get visual based on movie name")
x=st.text_input("Movie","Star Wars")
if st.button("Submit"):
  st.write(f"your favorite movie is '{x}'")
data=pd.read_csv("movies.csv")
st.write(data)
chart_data=pd.dataframe(np.random.randn(20,3), columns=["a","b","c"])
st.bar_chart(chart_data)

  
