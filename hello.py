import streamlit as st
import pandas as pd
import plotly.express as px

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

# Load data
df = pd.read_csv("inputfile.csv")
st.write(df)

# Create a copy of the DataFrame
df1 = df.copy()

# Convert CreationDate to datetime format and extract date
df1['Date'] = pd.to_datetime(df1['CreationDate']).dt.date

# Group by UserId, Date, and Operation to count occurrences
summary_df = df1.groupby(['UserId', 'Date', 'Operation']).size().reset_index(name='Count of Operations')

# Aggregate the count of operations by UserId
final_summary_df = summary_df.groupby('UserId').agg({
    'Date': 'first',
    'Operation': 'first',
    'Count of Operations': 'sum'
}).reset_index()

st.subheader("Operation Count by UserId, Date, and Operation")
st.table(final_summary_df[['UserId', 'Date', 'Operation', 'Count of Operations']])

# Create for Operation
st.sidebar.header("Choose your filter: ")
operation = st.sidebar.multiselect("Pick your operation", df["Operation"].unique())
if not operation:
    df2 = df.copy()
else:
    df2 = df[df["Operation"].isin(operation)]
    
col1, col2 = st.columns((2))
with col1:
    st.subheader("Count of operations by CreationDate")
    fig = px.bar(category_df, x = "CreationDate", y = "Operation", text = ['${:,.2f}'.format(x) for x in category_df["Sales"]],
                 template = "seaborn")
    st.plotly_chart(fig,use_container_width=True, height = 200)

with col2:
    st.subheader("RecordType by Operation")
    fig = px.pie(filtered_df, values = "RecordType", names = "Operation", hole = 0.5)
    fig.update_traces(text = filtered_df["Operation"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)

