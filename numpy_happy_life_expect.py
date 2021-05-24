import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



# https://www.kaggle.com/unsdsn/world-happiness
happydata = pd.read_csv('world-happiness-report-2021.csv')

#print(happydata.columns)

# Set variables to hold data to join into 2d numpy array
np_happyscore = happydata['Ladder score']
np_lifeexpect = happydata['Healthy life expectancy']

# Join the two sets of data into a numpy array
happyarray = np.column_stack([np_happyscore, np_lifeexpect])


#print(happyarray.shape)
#print(happyarray.ndim)
#print(happyarray[:,0])


print("The average happiness score in the 149 countries included was",np.mean(happyarray[:,0]))
print("The average life expectancy in the 149 countries included was",np.mean(happyarray[:,1]))

print("The median happiness score in the 149 countries included was",np.median(happyarray[:,0]))
print("The median life expectancy in the 149 countries included was",np.median(happyarray[:,1]))

print("The std.dev in happiness score in the 149 countries included was",np.std(happyarray[:,0]))
print("The std.dev in life expectancy in the 149 countries included was",np.std(happyarray[:,1]))

print("Pearson Correlation Coefficient between Happiness and Life Expectancy is", np.corrcoef(happyarray[:,0],happyarray[:,1]))

matplotlib.style.use('ggplot')
x= happyarray[:,0]
y= happyarray[:,1]
plt.scatter(x, y)

plt.xticks(fontsize=8)
plt.xlabel('Happy Score', fontsize=10)
plt.ylabel('Life Expectancy', fontsize=10)
plt.xticks(rotation=40)
plt.title('Correlation between Happiness and Life Expectancy')
plt.show()



