class Matrix:
    def __init__(self, list_1, list_2):
        self.matrix = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


my_matrix = Matrix([[7356, 53, 7643],
                    [635367, 3678, 35673],
                    [3568, 50745, 3673737]],
                   [[2456, 256645, 873676],
                    [98567, 23546, 93],
                    [234, 7365, 7569]])

print(my_matrix.__add__())
