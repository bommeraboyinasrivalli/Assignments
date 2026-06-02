#Write a Python Program to Multiply Two Matrices.

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0, 0],
          [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]

print("Result:")
for row in result:
    print(row)
