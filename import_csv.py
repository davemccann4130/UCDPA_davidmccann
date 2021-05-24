import pandas as pd


#https://www.kaggle.com/unsdsn/world-happiness
happydata = pd.read_csv('world-happiness-report-2021.csv')

#https://data.worldbank.org/indicator/SP.POP.TOTL
pop = pd.read_csv('sp_pop_total.csv')

#add 2020 pop data to happydata
pop19 = pop['2019']
happydata['2019'] = pop19

#pop = happydata['2019'].to_numpy()

#print(type(pop))
#print(pop)


#print(happydata.head())
#print(happydata.columns)
#print(happydata.info)

#print(pop.head())
#print(pop.columns)
#print(pop.info)

#print(happydata[['Ladder score']].mean())