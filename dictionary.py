import pandas as pd
import matplotlib.pylab as plt

#https://www.kaggle.com/unsdsn/world-happiness
happydata = pd.read_csv('world-happiness-report-2021.csv')

#https://data.worldbank.org/indicator/SP.POP.TOTL
pop = pd.read_csv('sp_pop_total.csv')

#https://data.worldbank.org/indicator/SP.POP.TOTL
pop2019 = pd.read_csv('pop_2019.csv')

#print(happydata.columns)
#print(pop2019.head())

# Merge the happydata and pop_2019 tables
happydata_pop2019 = happydata.merge(pop2019,on='Country name')

#set the Country name as the index for dictionary conversion in next step
happydata_index = happydata_pop2019.set_index('Country name')
#print(happydata_index.head())
#print(happydata_index.info())

#create the dictionary. The dataframe index 'Country name' is set as key and values set to 'Ladder score'
happydata_dict = happydata_index['Ladder score'].to_dict()
print(type(happydata_index))
print(type(happydata_dict))
#print(happydata_dict)
print(happydata_dict.keys())

min_happy = min(zip(happydata_dict.values(), happydata_dict.keys()))
max_happy = max(zip(happydata_dict.values(), happydata_dict.keys()))

#print(f"Output \n***{x,min_happy , max_happy} ")
print('Happiest Country: ', max_happy)
print('Saddest Country: ', min_happy)








