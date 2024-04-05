import random

matrix = [[random.randint(1, 100) for i in range(4)] for j in range(4)]
diagonal = [matrix[i][i] for i in range(4)]
print(matrix)
print(diagonal)
