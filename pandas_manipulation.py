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

#print(happy_df.head())
#print(happy_df.info())
#print(happy_df.describe())
#print(happy_df.shape)
#print(happy_df.values)
#print(happy_df.columns)
#print(happy_df.index)

# manually insert duplicate row as my dataframe has no duplicates
# - www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/amp/
# Check length before adding row
length1 = len(happy_df)
#print(length1)

# insertion of duplicate row at index 150
happy_df.loc[150] = [happy_df['Country name'][110],
                happy_df['Regional indicator'][110],
                happy_df['Ladder score'][110],
                happy_df['Standard error of ladder score'][110],
                happy_df['upperwhisker'][110],
                happy_df['lowerwhisker'][110],
                happy_df['Logged GDP per capita'][110],
                happy_df['Social support'][110],
                happy_df['Healthy life expectancy'][110],
                happy_df['Freedom to make life choices'][110],
                happy_df['Generosity'][110],
                happy_df['Perceptions of corruption'][110],
                happy_df['Ladder score in Dystopia'][110],
                happy_df['Explained by: Log GDP per capita'][110],
                happy_df['Explained by: Social support'][110],
                happy_df['Explained by: Healthy life expectancy'][110],
                happy_df['Explained by: Freedom to make life choices'][110],
                happy_df['Explained by: Generosity'][110],
                happy_df['Explained by: Perceptions of corruption'][110],
                happy_df['Dystopia + residual'][110],
                happy_df['2019'][110],
                happy_df['Continent'][110]]

# check length after adding duplicate row
length2 = len(happy_df)
#print(length2)

# drop the duplicate value again
happy_df.drop_duplicates(keep='first', inplace = True)

# check length after dropping duplicate row
length3 = len(happy_df)
#print(length3)

# sort the dataframe by population and print result
happy_df_pop_sort = happy_df.sort_values('2019', ascending = False)
#print(happy_df_pop_sort.head())

# sort the dataframe by continent then population (smallest to largest) and print result
happy_df_popconti_sort = happy_df.sort_values(['Continent','2019'], ascending = [True, True])
#print(happy_df_popconti_sort[['Country name','Continent','2019']].to_string())


# subset dataframe to show counties with population greater than 100 million, largest to smallest
happy_df_hundredmillionpop = happy_df[happy_df['2019'] > 100].sort_values('2019', ascending = False)
#print(happy_df_hundredmillionpop[['Country name','Continent','2019']].to_string())

# using .isin to return countries in Asia and Europe
isin_asia_europe = happy_df[happy_df['Continent'].isin(['Asia','Europe'])]
#print(isin_asia_europe[['Country name','Continent']].sort_values('Continent').to_string())

# print sad populous countries (>100 million pop with less than average happy score(5.532839))
sad_pop = happy_df[(happy_df['Ladder score'] < 5.532839) & (happy_df['2019'] > 100)].sort_values('2019', ascending = False)
#print(sad_pop[['Country name','2019','Ladder score']].to_string())


# looping with iterrows return all data - stackabuse.com/how-to-iterate-over-rows-in-a-pandas-dataframe
#for i, row in happy_df.iterrows():
    #print(f"Index: {i}")
    #print(f"{row}\n")

# looping with iterrows return specific data - stackabuse.com/how-to-iterate-over-rows-in-a-pandas-dataframe
for i, row in happy_df.iterrows():
    print(f"Index: {i}")
    print(f"{row[['Continent','Country name','2019']]}\n")