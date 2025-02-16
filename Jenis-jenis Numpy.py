import numpy as np
def topic_learn(kalimat):
    return print(kalimat)

# 1. Creating a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5, 6])
topic_learn('1. Creating a NumPy array from a list')
print(arr)


# 2. Creating arrays of zeros and ones
zeros = np.zeros(5)
ones = np.ones((2, 3))
topic_learn('\n2. Creating arrays of zeros and ones')
print(zeros)
print(ones)


# 3. Generating random numbers
random_arr = np.random.rand(3,3)
topic_learn('\n3. Generating random numbers')
print(random_arr)


# 4. Reshaping a 1D array into 2D
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape((2,3))
topic_learn('\n4. Reshaping a 1D array into 2D')
print(reshaped)


# 5. Accessing Element and slicing arrays
arr = np.array([10, 20, 30, 40, 50])
topic_learn('\n5. Accessing Element and slicing arrays')
print(arr[1])
print(arr[1:4])


# 6. Performing element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
topic_learn('\n6. Performing element-wise operations')
print(result)


# 7. Calculating mean, median, and standard deviation 
arr = np.array([1, 2, 3, 4, 5])
topic_learn('\n7. Calculating mean, median, and standard deviation')
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))


# 8. Broadcasting scalar to array
arr = np.array([1, 2, 3])
result = arr * 2
topic_learn('\n8. Broadcasting scalar to array')
print(result)


# 9. Filtering array elements using a condition 
arr = np.array([10, 20, 30, 40, 50])
result = arr[arr > 30]
topic_learn('\n9. Filtering array elements using a condition')
print(result)


# 10. Vectorized operation for fast computation
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = np.exp(arr)
topic_learn('\n10. Vectorized operation for fast computation')
print(result)


# 11. linear algebra operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

topic_learn('\n11. linear algebra operations')

result = np.dot(A, B)
print(result)

determinans = np.linalg.det(A)
print(determinans)


