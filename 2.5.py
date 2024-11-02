def get_matrix (n, m, value):

    matrix = []
    count = 0
    for el in range (0, n):
        x = []
        i = matrix.append(x)
        count += 1
        for el in range (0, m):
            j = matrix[(count -1)].append(value)
    count = 0
    return (matrix)


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)