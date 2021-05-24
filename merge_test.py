import pandas as pd

#https://www.kaggle.com/unsdsn/world-happiness
happydata = pd.read_csv('world-happiness-report-2021.csv')

#https://data.worldbank.org/indicator/SP.POP.TOTL
pop = pd.read_csv('sp_pop_total.csv')

#https://data.worldbank.org/indicator/SP.POP.TOTL
pop2019 = pd.read_csv('pop_2019.csv')

#print(happydata.columns)
#print(pop2019.head())


# Merge the happydata and pop_2019 tables on Country Name
happydata_pop2019 = happydata.merge(pop2019,on='Country name')


#print(happydata_pop2019.columns)
#print(happydata_pop2019.to_string())
print(happydata_pop2019['Regional indicator'].unique())
print(happydata_pop2019[happydata_pop2019['Regional indicator'] == "Western Europe"])