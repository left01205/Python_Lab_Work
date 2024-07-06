import pandas as pd

# Import CSV file into DataFrame
df = pd.read_csv('test.csv')

# (a) Visualize the first and last 10 records
print("First 10 records:")
print(df.head(10))
print("Last 10 records:")
print(df.tail(10))

# (b) Get the shape, index, and column details
print("Shape of DataFrame:", df.shape)
print("Index of DataFrame:", df.index)
print("Columns of DataFrame:", df.columns)

# (c) Select/Delete the records(rows)/columns based on conditions
# Example: Select rows where 'column_name' is greater than 10
selected_rows = df[df['column_name'] > 10]
# Example: Delete rows where 'column_name' is equal to 'some_value'
df = df[df['column_name'] != 'some_value']
# Example: Delete 'column_name' from DataFrame
df = df.drop('column_name', axis=1)

# (d) Perform ranking and sorting operations
# Example: Rank 'column_name' in ascending order
df['column_name_rank'] = df['column_name'].rank(ascending=True)
# Example: Sort DataFrame by 'column_name' in descending order
df = df.sort_values('column_name', ascending=False)

# (e) Do required statistical operations on the given columns
# Example: Calculate mean of 'column_name'
mean_value = df['column_name'].mean()
# Example: Calculate standard deviation of 'column_name'
std_value = df['column_name'].std()

# (f) Find the count and uniqueness of the given categorical values
# Example: Count the occurrences of each unique value in 'column_name'
value_counts = df['column_name'].value_counts()
# Example: Get the number of unique values in 'column_name'
unique_values = df['column_name'].nunique()

# (g) Rename single/multiple columns
# Example: Rename 'old_column_name' to 'new_column_name'
df = df.rename(columns={'old_column_name': 'new_column_name'})
# Example: Rename multiple columns
df = df.rename(columns={'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'})