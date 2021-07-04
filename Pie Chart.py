# Import packages required for Data Extraction
import pandas as pd
import matplotlib.pyplot as plt

# Import CSV as a Dataframe, index by Tournament Column (insert after filename, index_col=5)
filename = 'results.csv'
df = pd.read_csv(filename)

# determine Null Values
missing_val = df.isnull().sum()

# Creating a results column using indexing
df['result'] = 'draw'
df.loc[df['home_score'] > df['away_score'], 'result'] = 'home_win'
df.loc[df['away_score'] > df['home_score'], 'result'] = 'away_win'

# Checking the 'Result' column stats
# print(df.groupby('result')['result'].count())

# Chart the percentage of Home Wins, Away Wins and Draws
df.groupby('result')['result'].count().plot(kind='pie', autopct='%1.1f%%', figsize=(4,4))
plt.show()
