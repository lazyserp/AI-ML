import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# 3 ways to do it:
print(np.dot(A, B))  # Dot product
print(A @ B)         # @ operator (Python 3.5+)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.inner(x, y))  # 1*4 + 2*5 + 3*6 = 32
print(np.outer(x, y))  # Outer product matrix

#determinants and inverse
A = np.array([[1, 2],
              [3, 4]])

print(np.linalg.det(A))   # Determinant
print(np.linalg.inv(A))   # Inverse

#EigenValues and EigenVectors
vals, vecs = np.linalg.eig(A)
print("Eigenvalues:", vals)
print("Eigenvectors:\n", vecs)

#vector length
v = np.array([3, 4])
print(np.linalg.norm(v))  # sqrt(3² + 4²) = 5

#solve eqns
coeffs = np.array([[2, 1],
                   [1, -1]])
const = np.array([5, 1])

#2x+y = 5
#x-y = 1

solution = np.linalg.solve(coeffs, const)
print(solution)  # [2. 1.]



#RANDOM MODULE 

np.random.seed(42)  # Makes results reproducible

# Uniform distribution [0, 1)
print(np.random.rand(3, 2))  

# Standard normal distribution (mean=0, std=1)
print(np.random.randn(3, 2))  

# Random integers
print(np.random.randint(0, 10, (2, 4)))  # ints from 0–9

arr = np.arange(10)
np.random.shuffle(arr)   # In-place shuffle
print(arr)

#Sampling and repalcemetn
arr = np.array([1, 2, 3, 4, 5])
sample = np.random.choice(arr, size=3, replace=False)
print(sample)

#




#DATA HANDLING
#splitting
arr = np.arange(1, 10)
print(np.split(arr, 3))         # 3 equal parts
print(np.array_split(arr, 4))   # Unequal allowed


#unqiue values
arr = np.array([1, 2, 2, 3, 4, 4, 4])
unique_vals = np.unique(arr)
vals, counts = np.unique(arr, return_counts=True)
print(unique_vals)    # [1 2 3 4]
print(counts)         # [1 2 1 3]


