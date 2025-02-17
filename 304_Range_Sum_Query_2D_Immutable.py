from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            sum = 0
            for j in range(cols):
                sum += matrix[i][j]
                matrix[i][j] = sum
        
        prefixMatrix = [[0 for i in range(cols)] for j in range(rows)]

        for j in range(cols):
            sum = 0
            for i in range(rows):
                sum += matrix[i][j]
                prefixMatrix[i][j] = sum

        print(prefixMatrix)
        print()
        self.prefixMatrix = prefixMatrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        up, left, corn = 0, 0, 0

        if row1 - 1 > -1 and col2 > -1:
            up = self.prefixMatrix[row1 -1][col2]
        if col1 - 1 > -1 and row2 > -1:
            left = self.prefixMatrix[row2][col1 - 1]
        if row1 -1 > -1 and col1 -1 > -1:
            corn = self.prefixMatrix[row1 - 1][col1 - 1]

        x = self.prefixMatrix[row2][col2]
        print(x, up, left, corn)
        print(row2 - 1, col1)
        print(self.prefixMatrix[row2 -1][col1])

        return x - up - left + corn

        


# Your NumMatrix object will be instantiated and called as such:
matrix = [[1,1,1], [1,1,1], [1,1,1]]
obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(0, 0, 2, 2)
param_2 = obj.sumRegion(1, 1, 2, 2)
# param_3 = obj.sumRegion(2, 2, 2, 2)

print(param_2)