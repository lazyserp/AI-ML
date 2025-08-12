import numpy as np

arr3d = np.arange(4).reshape(2, 2)
print(arr3d)
print(np.swapaxes(arr3d, 0, 1) ) # Changes the axis order

#MATHEMATICS OF NUMPY
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(np.sum(arr))         # 21 (sum of all elements)
print(np.mean(arr))        # 3.5 (average)
print(np.std(arr))         # Standard deviation
print(np.var(arr))         # Variance
print(np.min(arr))         # 1
print(np.max(arr))         # 6
print(np.median(arr))      # 3.5
print(np.argmin(arr))      # 0 (index of min value)
print(np.argmax(arr))      # 5 (index of max value)

#row wise ops
print(np.sum(arr, axis=0))  # Column sums → [5 7 9]
print(np.sum(arr, axis=1))  # Row sums → [6 15]

arr = np.array([1, 4, 9])

print(np.sqrt(arr))  # [1. 2. 3.]
print(np.exp(arr))   # e^arr
print(np.log(arr))   # natural log
print(np.sin(arr))   # sine values
print(np.cos(arr))   # cosine values
