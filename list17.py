
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]


print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nSum of Matrix A and B:")
for row in C:
    print(row)