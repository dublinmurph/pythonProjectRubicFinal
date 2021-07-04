# Import packages required for Data Extraction
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
# df.groupby('result')['result'].count().plot(kind='pie', autopct='%1.1f%%', figsize=(4,4))

# Create a column for the total goals scored
df['total_goals'] = df['away_score'] + df['home_score']

# Chart the Sum of the number of goals scored per year
# df.groupby('date')['total_goals'].sum().plot()
# plt.xlabel("Year")
# plt.ylabel("No. of Goals")
# plt.title("Sum of Goals per Year")

# Chart The average number of total goals per year is slowly but steadily increasing
# avg_goals_per_season = df.groupby('date')['total_goals'].mean().reset_index()
# avg_goals_per_season['date'] = avg_goals_per_season['date'].map(lambda s: int(s[:4]))
# sns.regplot(x='date', y='total_goals', data=avg_goals_per_season)
# plt.show()

# Chart the number of games per month by converting the date column to a Datetime format
df['game_date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
df['game_month'] = df['game_date'].dt.month
df['game_weekday'] = df['game_date'].dt.weekday

#df.groupby([df['game_date'].dt.month])['result'].count().plot(kind='bar')
# plt.xlabel("Months")
# plt.ylabel("No. of Games")
# plt.title("Total Number of Games per Month")

# Chart Showing number of goals per month
# sns.boxplot(x='game_month', y='total_goals', data=df)
# plt.title("Goals per Month")

# Chart Showing Goals grouped by the Days of The Week
# sns.boxplot(x='game_weekday', y='total_goals', data=df)
# plt.title("Goals per Day of The Week")
# plt.show()

# Chart showing the number of Games per Weekday
df.groupby('game_weekday')['result'].count().plot(kind='bar')
plt.title("Number of Games per Day")
plt.show()
