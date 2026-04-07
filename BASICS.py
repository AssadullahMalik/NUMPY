import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.zeros((2, 3))
arr3 = np.ones((3, 3))
arr4 = np.arange(0, 10, 2)
arr5 = np.linspace(0, 1, 5)

print("Array:", arr1)
print("Zeros:\n", arr2)
print("Ones:\n", arr3)
print("Range:", arr4)
print("Linspace:", arr5)

# Attributes
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Data Type:", arr1.dtype)
print("Dimensions:", arr1.ndim)
