import pandas as pd

import matplotlib.pyplot as plt

# (a) Import CSV file to DataFrame
df = pd.read_csv('test.csv')

# (a) Handle missing data
df.dropna()  # Drop rows with missing values
df.fillna(value)  # Fill missing values with a specific value

# (b) Transform data using apply() and map()
df['column_name'].apply(function)  # Apply a function to a column
df['column_name'].map(dictionary)  # Map values using a dictionary

# (c) Detect and filter outliers
def detect_outliers(data):
    # Implement outlier detection logic here
    return outliers

outliers = detect_outliers(df['column_name'])
filtered_df = df[~df['column_name'].isin(outliers)]

# (d) Perform Vectorized String operations
df['column_name'].str.method()  # Perform string operations on a column

# (e) Visualize data
df.plot.line(x='x_column', y='y_column')  # Line plot
df.plot.bar(x='x_column', y='y_column')  # Bar plot
df.plot.hist()  # Histogram
df.plot.kde()  # Density plot
df.plot.scatter(x='x_column', y='y_column')  # Scatter plot

plt.show()  # Show the plots