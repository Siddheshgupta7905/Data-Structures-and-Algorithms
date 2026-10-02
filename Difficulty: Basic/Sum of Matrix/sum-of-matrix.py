class Solution:
    def sumOfMatrix(self, mat: list[list[int]]) -> int:
        # code here
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                total += mat[i][j]
        return total