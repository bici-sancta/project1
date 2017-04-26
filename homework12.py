
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ...	 description
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""

Week 12 - Homework for MSDS Data Science 6306

Patrick McDevitt
25-Apr-2017

"""


#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ...	imports
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


import math
import copy
import csv

#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ...	question 1
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

q1_list = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]

print(q1_list)

print(q1_list[4])

q1_list.append(55.2)

print(q1_list)

q1_list.pop(5)

print(len(q1_list))


for i in range(0, len(q1_list)):
	if q1_list[i] > 45:
		print(q1_list[i])



#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ...	question 2
#		2. Introduction to numpy –
#			a. Import the numpy library using the following command – import numpy
#			b. Declare numpy array with the same data points as in my_list using numpy.array()
#			c. Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
#			d. Use logical referencing to get only those values that are less than 45
#			e. Compute the max and min of the array using numpy.max() and numpy.min()
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import numpy as np

np_a = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
print(np_a)

avg = np_a.mean()
std = np_a.std()

print ("avg = ", avg)
print ("standard deviation = ", std)


filterData = np_a[np_a < 45]

print(filterData)

xxx_max = np_a.max()
xxx_min = np_a.min()

print ("max = ", xxx_max)
print ("min = ", xxx_min)


#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ...	question 3
#
#		Introduction to pandas –
#			a. Import the pandas library – import pandas
#			b. Read the IRIS dataset into iris using pandas.read_csv(). Data file –
#			c. Using iris.head(), display the head of the dataset
#			d. Use DataFrame.drop() to drop the id column


# from : http://stackoverflow.com/questions/20107570/removing-index-column-in-pandas
# DataFrames and Series always have an index. Although it displays alongside the column(s), it is not a column, which is why del df['index'] did not work.
# If you want to replace the index with simple sequential numbers, use df.reset_index(). I strongly suggest reading a little bit of the pandas documentation, like 10 minutes to Pandas to get a sense for why the index is there is how it is used.


#			e. Subset dataframe to create a new data frame that includes only the measurements for the setosa species
#			f. Use DataFrame.describe() to get the summary statistics
#			g. Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
#			h. Use DataFrame.boxplot() to plot boxplots by Species

#			i. Plot a scatter matrix plot using the seaborn library. Use the following to load and plot
#			i. Import seaborn
#			ii. Seaborn.pairplot(dataframe,by=’column_name’)
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(iris.head(20))

print(iris)


setosa = iris.loc[iris['species'] == 'setosa']

print(setosa)

print(setosa.describe())

print(iris.groupby(['species']).describe())

iris.groupby(['species']).boxplot()


# ...import seaborn as sns

# .. for whatever unknown reason, seaborn does not install on my computer
# ...	will have to fight this another day


# ...	end ...
#	-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-




