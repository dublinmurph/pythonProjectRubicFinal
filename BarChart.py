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

# Create a column for the total goals scored
df['total_goals'] = df['away_score'] + df['home_score']

# Chart the number of games per month by converting the date column to a Datetime format
df['game_date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
df['game_month'] = df['game_date'].dt.month
df['game_weekday'] = df['game_date'].dt.weekday

# Group results by month
df.groupby([df['game_date'].dt.month])['result'].count().plot(kind='bar')
plt.xlabel("Months")
plt.ylabel("No. of Games")
plt.title("Total Number of Games per Month")
plt.show()
