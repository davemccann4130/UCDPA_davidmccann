import pandas as pd
import numpy as np

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

# Average happiness per continent sorted largest to smallest score
continent_mean_happy = happy_df.groupby('Continent')['Ladder score'].mean().sort_values(ascending = False)
#print(continent_mean_happy)

# median happiness per continent sorted largest to smallest score
continent_median_happy = happy_df.groupby('Continent')['Ladder score'].median().sort_values(ascending = False)
#print(continent_median_happy)

# Continent Min and Max Happy Scores
continent_minmax_happy = happy_df.groupby('Continent')['Ladder score'].agg([min,max])
print(continent_minmax_happy)

# use pivot_table to display continents by min , max , mean , median.
continent_pivot = happy_df.pivot_table(values = 'Ladder score', index = 'Continent', aggfunc = [np.min, np.max, np.mean, np.median])
print(continent_pivot)
