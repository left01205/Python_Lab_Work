import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series from a list:")
print(series)

# Creating a Series from a dictionary
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series = pd.Series(data)
print("\nSeries from a dictionary:")
print(series)

# Creating a DataFrame from a list of lists
data = [['John', 25], ['Jane', 30], ['Dave', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print("\nDataFrame from a list of lists:")
print(df)

# Creating a DataFrame from a dictionary of lists
data = {'Name': ['John', 'Jane', 'Dave'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("\nDataFrame from a dictionary of lists:")
print(df)