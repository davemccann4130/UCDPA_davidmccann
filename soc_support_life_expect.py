import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib. pyplot as plt

# read csv into dataframe
happydata = pd.read_csv('world-happiness-report-2021.csv')

# sort by happiness score
happydata_sort = happydata.sort_values('Ladder score', ascending = False)

#print(happydata.head())
#print(happydata.columns)
#print(happydata_sort.head())


socsupport_life = happydata[['Social support','Healthy life expectancy']]

slope, intercept, r_value, p_value, std_err = stats.linregress(socsupport_life['Social support'],socsupport_life['Healthy life expectancy'])


print('The linear coefficient (r-Value) of Social Support to Life Expectancy is',r_value)
print('The probability value (p-Value) of Social Support to Life Expectancy is', p_value)
#print(slope)
#print(intercept)
#print(std_err)

x = socsupport_life['Social support']
y = socsupport_life['Healthy life expectancy']

# plot the correlation
sns.regplot(x=x, y=y, scatter_kws={"color": "black"},line_kws={"color": "red"})

# set the title
plt.title('Linear Coefficient of Social Support and Life Expectancy')
# Set x-axis label
plt.xlabel('Social support')
# Set y-axis label
plt.ylabel('Healthy life expectancy')

plt.show()

