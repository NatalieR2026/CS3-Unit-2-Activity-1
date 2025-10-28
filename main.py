import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())

print(df.shape)
print(df.info()) # summary of columns

# Filter films that cost over a million dollars
# df['budget'] grab the column you want
budget_df = df[ df['budget'] > 1000000 ]
print(budget_df.shape) # 7208 movies have a budget above 1mil

# Create a series from the budget column
# that uses the title column for the indices
budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'])
print(budget_lookup) # now we can look up budgets by movie title
print(budget_lookup['Avatar']) # 237 mil

# First define the condition to be checked
# budget_lookup.index is the title of the movie
condition = (budget_lookup.index >= 'A Bag of Hammers') & (budget_lookup.index )
