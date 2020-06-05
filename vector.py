import numpy as np

# gives rank 1 array
a = np.random.randn(5)
print(a)

# shape = (5,) is neither row or col
print(a.shape)

# same as a
print(a.T)

# not a matrix but number
print(np.dot(a, a.T)) 

# gives 5x1 vector 
a = np.random.randn(5, 1)
print('vector:', a)
print('trans:', a.T)
print('dot:\n', np.dot(a, a.T))