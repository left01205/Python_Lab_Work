import numpy as np


arr = np.array([1, 2, 3, 4, 5])

squared = np.square(arr)  
cubed = np.power(arr, 3)  
sqrt = np.sqrt(arr)  
log = np.log(arr)  
exp = np.exp(arr)  

print("Original array:", arr)
print("Squared array:", squared)
print("Cubed array:", cubed)
print("Square root array:", sqrt)
print("Natural logarithm array:", log)
print("Exponential array:", exp)