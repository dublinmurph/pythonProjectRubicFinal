import pandas as pd

# Import CSV as a Dataframe, index by Tournament Column
filename = 'results.csv'
df = pd.read_csv(filename, index_col=5)

# determine Null Values
missing_val = df.isnull().sum()

# Check Data Types
# print(df.dtypes)

# Clean Data
cleaned_data = df.dropna(axis=0)

# Sort Data
sort = df.sort_values(by='date', ascending=False)

# Convert df to a List
df_list = df.values.tolist()

print(df_list)
