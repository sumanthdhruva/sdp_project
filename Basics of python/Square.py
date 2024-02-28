#Example 4
import numpy as np
# Creating a NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Basic operations on arrays
sum_arr1 = np.sum(arr1)
mean_arr2 = np.mean(arr2)

print("Sum of 1D Array:", sum_arr1)
print("Mean of 2D Array:", mean_arr2)

# Element-wise operations
squared_arr1 = np.square(arr1)
sqrt_arr2 = np.sqrt(arr2)

print("Squared elements of arr1:", squared_arr1)
print("Square root of arr2:", sqrt_arr2)