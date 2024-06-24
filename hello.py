import streamlit as st
import pandas as pd
import numpy as np
st.write("My name is varalakshmi")
st.write("Get visual based on movie name")
x=st.text_input("Movie"."Star Wars")
if st.button("Submit"):
  st.write(f"your favorite movie is '{x}'")
  
