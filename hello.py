import pandas as pd

# URL of the penguin dataset CSV file on GitHub
url = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv'

# Load the dataset into a pandas DataFrame
penguins = pd.read_csv(url)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(penguins.head())

# Create a summary table grouped by island and species
summary_table = penguins.groupby(['island', 'species']).size().reset_index(name='count')

# Display the summary table
print("\nSummary table by island and species:")
print(summary_table)




