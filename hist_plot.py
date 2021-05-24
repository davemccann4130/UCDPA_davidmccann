import pandas as pd
import matplotlib.pyplot as plt

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

print(happydata_pop2019.info())
print(happydata_pop2019.head())
print(happydata_pop2019.shape)

happydata_hist = happydata_pop2019[['Ladder score','Logged GDP per capita','Healthy life expectancy','Social support']]
happydata_hist.hist(bins=25, grid=False, color='#86bf91', zorder=2, rwidth=0.9)
plt.show()