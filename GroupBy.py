# Import packages required for Data Extraction
import pandas as pd

# Import CSV as a Dataframe, index by Tournament Column
filename = 'results.csv'
df = pd.read_csv(filename, index_col=5)

# determine Null Values
missing_val = df.isnull().sum()

# Clean Data
cleaned_data = df.dropna(axis=0)

# Group Data
grp = df.groupby('home_team')

print(grp.head())
