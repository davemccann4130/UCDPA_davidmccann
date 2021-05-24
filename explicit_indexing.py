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

# set a the country name column as the index
happy_df_ind = happy_df.set_index('Country name')
#print(happy_df_ind.index)

# undo the above index if needed
#happy_df_ind = happy_df_ind.reset_index(drop = True)
#print(happy_df_ind.index)

# subsetting using the Country Name index and .loc
#print(happy_df_ind.loc[['Ireland','Botswana']])

# set multi level index
happy_df_multi_ind = happy_df.set_index(['Continent','Country name'])
#print(happy_df_multi_ind.index)

# subset using multi level index
#print(happy_df_multi_ind.loc[[('Ireland','Europe'),('Botswana','Africa')]])

# sorting by indexes set above
happy_df_multi_ind_sorted = happy_df_multi_ind.sort_index(level = ['Continent', 'Country name'], ascending =[True, True])
#print(happy_df_multi_ind_sorted)
