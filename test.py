import numpy as np

array = np.array([
    [3, 2, -6, -3, -6],
    [-3, -5, 1, 3, -5],
    [3, 2, 2, -1, 2],
    [-3, 1, -5, -1, -3],
])
# [[3, 2],
#  [-3, -5],
#  [3, 2],
#  [-3, 1], ]
array_t = np.transpose(array)
print(array_t[[1, 2]])
