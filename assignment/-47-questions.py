# List of lists representing a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix using zip
transposed_matrix = list(map(list, zip(*matrix)))

# Print the result
print('Original Matrix:')
for row in matrix:
    print(row)

print('\nTransposed Matrix:')
for row in transposed_matrix:
    print(row)


import numpy as np

# List of lists representing a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convert the list of lists to a numpy array
matrix_np = np.array(matrix)

# Transpose the matrix using numpy
transposed = matrix_np.T

# Print the result
print('Original Matrix:')
print(matrix_np)

print('Transposed Matrix:')
print(transposed)
