import numpy as np

# 1. ARRAY CREATION & INITIALIZATION
# Basic Array
arr = np.array([1, 2, 3, 4, 5])
print("Basic Array:", arr)

# Zeros, Ones, and Empty Arrays
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
empty = np.empty((2, 3))
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Empty Array:\n", empty)

# Identity Matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# Arange and Linspace
arange_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)
print("Arange Array:", arange_arr)
print("Linspace Array:", linspace_arr)

# Random Arrays
rand_arr = np.random.random((2, 2))
rand_ints = np.random.randint(0, 10, (2, 2))
print("Random Array:\n", rand_arr)
print("Random Integers:\n", rand_ints)

# 2. MATHEMATICAL OPERATIONS
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise Operations
print("Addition:", np.add(arr1, arr2))
print("Subtraction:", np.subtract(arr2, arr1))
print("Multiplication:", np.multiply(arr1, arr2))
print("Division:", np.divide(arr2, arr1))

# Aggregate Functions
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))

# Exponential and Logarithmic
print("Exponential:", np.exp(arr1))
print("Logarithm:", np.log(arr1))

# 3. ARRAY MANIPULATION
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)

# Reshape
reshaped = arr.reshape(3, 2)
print("Reshaped Array:\n", reshaped)

# Transpose
transposed = np.transpose(arr)
print("Transposed Array:\n", transposed)

# Flatten
flattened = arr.flatten()
print("Flattened Array:", flattened)

# Concatenation
concat = np.concatenate((arr1, arr2))
print("Concatenated Array:", concat)

# Stacking
stacked = np.vstack((arr1, arr2))
print("Vertically Stacked Array:\n", stacked)

# 4. STATISTICAL FUNCTIONS
data = np.array([[1, 2, 3], [4, 5, 6]])

# Statistics
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Median:", np.median(data))

# 5. INDEXING AND SLICING
sliced = data[0:2, 1:3]  # Slicing rows and columns
print("Sliced Array:\n", sliced)

# Boolean Masking
bool_mask = data > 3
print("Boolean Mask:\n", bool_mask)
print("Values greater than 3:\n", data[bool_mask])

# 6. LINEAR ALGEBRA OPERATIONS
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

# Matrix Multiplication
matrix_product = np.dot(A, B)
print("Matrix Product:\n", matrix_product)

# Determinant
det = np.linalg.det(A)
print("Determinant of A:", det)

# Inverse
inv = np.linalg.inv(A)
print("Inverse of A:\n", inv)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# 7. UTILITY FUNCTIONS
# Sorting
sorted_arr = np.sort(arr1)
print("Sorted Array:", sorted_arr)

# Unique
unique_vals = np.unique([1, 2, 2, 3, 3, 4])
print("Unique Values:", unique_vals)

# Where Condition
condition = np.where(arr1 > 2, "Greater", "Smaller")
print("Where Condition Result:", condition)

# Copy and View
original = np.array([1, 2, 3])
copy_arr = original.copy()
view_arr = original.view()
print("Original:", original, "Copy:", copy_arr, "View:", view_arr)

# Shape and Size
print("Shape:", original.shape)
print("Size:", original.size)
