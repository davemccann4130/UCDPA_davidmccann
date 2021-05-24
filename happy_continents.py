import pandas as pd
import matplotlib. pyplot as plt
import seaborn as sns

#https://www.kaggle.com/unsdsn/world-happiness
happydata = pd.read_csv('world-happiness-report-2021.csv')
#print(happydata.columns)

# read in the country_continent
country_continent = pd.read_csv('country_continent.csv')

# Merge the happydatapop and country continent tables
happydata_conti = happydata.merge(country_continent,on='Country name')

sns.set(style="darkgrid")

#sns.boxplot(x='Continent', y='Ladder score', palette="Blues", data=happydata_conti)
#sns.boxenplot(x='Continent', y="Ladder score", data=happydata_conti)
sns.violinplot(x='Continent', y="Ladder score", data=happydata_conti)
#sns.stripplot(x='Continent', y="Ladder score", data=happydata_conti)
sns.relplot(x='Continent', y='Ladder score', hue='Ladder score', legend= False, data=happydata_conti)
plt.xticks(fontsize=8)
plt.xlabel('Continent', fontsize=10)
plt.ylabel('Happy Score', fontsize=10)
plt.xticks(rotation=40)
plt.title('Happiness by Continent')
plt.tight_layout()
plt.show()