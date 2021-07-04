# Import packages required for Data Extraction
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Import CSV as a Dataframe, index by Tournament Column (insert after filename, index_col=5)
filename = 'results.csv'
df = pd.read_csv(filename)

# determine Null Values
missing_val = df.isnull().sum()

# Clean Data
cleaned_data = df.dropna(axis=0)

# Sort Data
sort = df.sort_values(by='date', ascending=False)

# Group Data
grp = df.groupby('home_team')

# Indexing by Column Headers, Select all data for the headers listed below
var = df[['home_team', 'home_score', 'away_team', 'away_score', 'date']]

# Slicing a subset of Rows using iloc method. print all rows from Column 0 to 5 inclusive.
# Note how city replaces tournament due to previous indexing by column 5
slc = df.iloc[0:, 0:6]

# Convert a single 'Date' String to datetime
date_object = datetime.strptime('1872-11-30', '%Y-%m-%d')

# print(date_object)

# Convert the 'Date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Pull results since my DOB (results that are greater than start date and smaller than end date
mask = (df['date'] > '1978-8-9') & (df['date'] <= '2021-06-30')

# Create Sub Dataframe
alive = df.loc[mask]

# Creating a results column
df['result'] = 'draw'
df.index[df['home_score'] > df['away_score'], 'result'] = 'home_win'
df.index[df['away_score'] > df['home_score'], 'result'] = 'away_win'

df.groupby('result')['result'].count()

plt.plot(alive)
plt.axis(['date', 'tournament'])
plt.show()
