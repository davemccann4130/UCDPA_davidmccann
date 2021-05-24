import pandas as pd
import numpy as np
import matplotlib. pyplot as plt
import seaborn as sns
import mplcursors

# an attempt on a variant of the Hans Rosling bubble plot using datacamp as a guide

# https://www.kaggle.com/unsdsn/world-happiness
happydata = pd.read_csv('world-happiness-report-2021.csv')

# https://data.worldbank.org/indicator/SP.POP.TOTL
pop = pd.read_csv('sp_pop_total.csv')

# https://data.worldbank.org/indicator/SP.POP.TOTL
pop2019 = pd.read_csv('pop_2019.csv')
# print(pop2019.info())

# read in the country_continent
country_continent = pd.read_csv('country_continent.csv')

# Merge the happydata and pop_2019 tables
happydata_pop = happydata.merge(pop2019,on='Country name')

# Merge the happydatapop and country continent tables and pop_2019 tables
happydata_pop_conti = happydata_pop.merge(country_continent,on='Country name')

# convert 2019 pop data to numpy array
np_pop = happydata_pop_conti['2019'].to_numpy()
# print(type(np_pop))

# set a multiplier on np_pop to get the markers to size i want - s in plot set to this variable
np_pop = np_pop * 6

# create the scatter plot
sns.scatterplot('Logged GDP per capita', 'Ladder score', data=happydata_pop_conti, hue='Continent',s=np_pop, alpha=0.8,
                legend='auto',palette='colorblind')

# Label and Title Strings
xlab = 'Logged GDP per Capita'
ylab = 'Happiness Score'
title = 'Happiness vs GDP vs Population'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Add grid() call
plt.grid(True,alpha=0.2)

# customise the legend
plt.legend(fontsize='8',loc='lower right')

# add tight layout to prevent ticks being cut off
plt.tight_layout()

#https://mplcursors.readthedocs.io/en/stable/examples/hover.html
#https://mplcursors.readthedocs.io/en/stable/examples/bar.html
# display annotation on plot when hovering over marker
mplcursors.cursor(hover=mplcursors.HoverMode.Transient).connect(
    "add", lambda sel: sel.annotation.set_text(happydata_pop_conti["Country name"][sel.target.index]))


# After customizing, display the plot
plt.show()

