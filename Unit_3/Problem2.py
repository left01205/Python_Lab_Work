import numpy as np

# Indexing of array
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # Output: 1

# Slicing of array
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # Output: [2 3 4]

# Reshaping of an array
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Joining two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
joined_arr = np.concatenate((arr1, arr2))
print(joined_arr)  # Output: [1 2 3 4 5 6]

# Splitting array
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)
print(split_arr)
# Output:
# [array([1, 2]), array([3, 4]), array([5, 6])]