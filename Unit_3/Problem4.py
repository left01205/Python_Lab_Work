import pandas as pd
import numpy as np

# Read the CSV file
data = np.genfromtxt('Records.csv', delimiter=',')

# Perform statistical operations
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

# Perform comparison operations
max_value = np.max(data)
min_value = np.min(data)
greater_than_5 = data[data > 5]

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Max Value:", max_value)
print("Min Value:", min_value)
print("Values greater than 5:", greater_than_5)