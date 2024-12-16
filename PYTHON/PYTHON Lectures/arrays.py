#------- ARRAYS------


# QUESTION
#Consider a random numpy array with elements [(10,20,30,40,50)]
import numpy as np
import pandas as pd
array = np.array([10,20,30,40,50])
print(array)

#Compute and display the mean of the array.

mean = np.mean(array)
print(mean)


#Compute and display the median.
median = np.median(array)
print(median)


#Write out the min and max values of the array.
minimum = np.min(array)
print(minimum)


maximum = np.max(array)
print(maximum)

#Display the standard deviation of the array.
standard_deviation = np.std(array)
print(standard_deviation)