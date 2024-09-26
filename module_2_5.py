def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
   return matrix

print(get_matrix(n: 2, m: 2, value: 10))
print(get_matrix(n: 3, m: 5, value: 42))
print(get_matrix(n: 4, m: 2, value: 13))
