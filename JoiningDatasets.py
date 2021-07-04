# Import packages required for Data Extraction
import pandas as pd

# Read .CSV files
year_1 = pd.read_csv("2018.csv")
year_2 = pd.read_csv("2019.csv")

merged_happiness = pd.merge(year_1, year_2, how='outer', on='Overall rank', suffixes=('_18,', '_19'), indicator=True)

print(merged_happiness.info())