import pandas as pd

# URL of the penguin dataset CSV file on GitHub
url = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv'

# Load the dataset into a pandas DataFrame
penguins = pd.read_csv(url)

# Display the first few rows of the dataset
print(penguins.head())




