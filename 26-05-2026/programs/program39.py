#Write a Python Program to Transpose a Matrix

matrix = [[1, 2],
          [3, 4]]

transpose = [[0, 0],
             [0, 0]]

for i in range(2):
    for j in range(2):
        transpose[j][i] = matrix[i][j]

print("Transpose Matrix:")
for row in transpose:
    print(row)
