# Import packages required for Data Extraction
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Chart The average number of total goals per year is slowly but steadily increasing
avg_goals_per_season = df.groupby('date')['total_goals'].mean().reset_index()
avg_goals_per_season['date'] = avg_goals_per_season['date'].map(lambda s: int(s[:4]))
sns.regplot(x='date', y='total_goals', data=avg_goals_per_season)
plt.show()
