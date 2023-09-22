def fill_diagonal(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
            elif i < j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 2


print("Введите размер матрицы")
n = input()
if n.isdigit() and n != "0":
    n = int(n)
    matrix = [[0] * n for _ in range(n)]
    fill_diagonal(matrix)
    for row in matrix:
        print(row)
else:
    print("Число должно быть натуральным")
