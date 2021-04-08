# 1. Реализовать класс Matrix (матрица).
class Matrix:
    def __init__(self, nested_list):
        self.rows = nested_list
        self.columns = [[nested_list[i][j] for i in range(len(nested_list))] for j in range(len(nested_list[0]))]
        self.shape = (len(nested_list), len(nested_list[0]))

    def __str__(self):
        return "".join(['\n'+''.join([str(el) + '   ' for el in row]) for row in self.rows])

    def __add__(self, other):
        return Matrix(list(list(map(sum, zip(self.rows[row], other.rows[row]))) for row in range(len(self.rows))))


mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat2 = Matrix([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(mat1)
print(mat1.shape)
print(mat1.columns)
print(mat1 + mat2)



