import pandas as pd

# URL of the penguin dataset CSV file on GitHub
url = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv'

# Load the dataset into a pandas DataFrame
penguins = pd.read_csv(url)

# Display the first few rows of the dataset
print(penguins.head())

# Page configuration should be set before any Streamlit elements are created
st.set_page_config(
    page_title="png",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

