import numpy as np

#create Array
npArray = np.array([1,2,3,4])

#array with zeroes and 2 rows and 3 coumns
zeros = np.zeros((2,3))

#array with ones and 2 rows and 3 coumns
ones = np.ones((4,5))

#array with given val and rwos and cols
vals = np.full((4,5),7)

# start=0, stop=10, step=2
a = np.arange(0, 10, 2)

# ints between 0-9
randint_arr = np.random.randint(0, 10, (2, 4))         
randn_arr = np.random.randn(2, 3) # Normal distribution (mean=0, std=1)




arr = np.array([1,2,3,4,5])
#Array Attributes
arr.shape
arr.ndim
arr.size
arr.dtype



#Arrays,slicing work like that in python
# print array values that match conditon

arr = np.array([2,4,6,8])
mask = arr  < 25 
print(mask)
print(arr[mask])



#element wise arithmetic
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # [4 10 18]
print(a / b)  # [0.25 0.4 0.5]
print(a ** 2) # [1 4 9]


#broadcasting
a = np.array([1, 2, 3])
print(a + 5)   # [6 7 8]  (scalar is “stretched”)


#logical ops
arr = np.array([10, 20, 30, 40])
print(np.logical_and(arr > 15, arr < 35))  # [False  True  True False]



#SHAPE MANIPULATION

#Array Reshaping
arr = np.arange(1,7)
reshaped = arr.reshape(2,3)
print(reshaped)

#Array flatenning
arr2d = np.array([ [1,2,3],[4,5,6] ])

print(arr2d.ravel())    # View (changes affect original)
print(arr2d.flatten())  # Copy (changes won't affect original)


#Add a dimension → useful for batch size in ML.
arr = np.array([1, 2, 3])
arr2d = arr[:, np.newaxis]  # Shape: (3, 1)
print(arr2d)

#transpose or swap axes
mat = np.array( 
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(mat.T)