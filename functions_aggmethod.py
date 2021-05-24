import pandas as pd

# https://www.kaggle.com/unsdsn/world-happiness
happy = pd.read_csv('world-happiness-report-2021.csv')

# https://data.worldbank.org/indicator/SP.POP.TOTL
pop = pd.read_csv('pop_2019.csv')
# print(pop2019.info())

# read in the country_continent
continent = pd.read_csv('country_continent.csv')

# Merge the happydata and pop_2019 df's
happy_pop = happy.merge(pop,on='Country name')

# Merge the happydatapop and country continent tables and pop_2019 tables
happy_df = happy_pop.merge(continent,on='Country name')

# define function to find 25th percentile of a column
def pct25(column):
    return column.quantile(0.25)

# define function to find 50th percentile of a column
def pct50(column):
    return column.quantile(0.50)

# Print 25th percentile of one column (population)
#print(happy_df[['2019']].agg(pct25))

# Print 25th percentile of two columns (population and happy score)
#print(happy_df[['2019','Ladder score']].agg(pct25))

# pass two functions to .agg method
#print(happy_df[['2019']].agg([pct25,pct50]))

# 2 columns and pass two functions to .agg method
print(happy_df[['2019','Ladder score']].agg([pct25,pct50]))

# cumulative sum function
#print(happy_df[['Ladder score']].cumsum())

# cumulative max function
#print(happy_df[['Ladder score']].cummax())

# cumulative min function
#print(happy_df[['Ladder score']].cummin())

# cumulative product function
#print(happy_df[['Ladder score']].cumprod())