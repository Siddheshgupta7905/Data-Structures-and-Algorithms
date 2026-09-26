class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:       
        matrix = []

        # Create n x n matrix filled with 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # 1. Left → Right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1

            top += 1

            # 2. Top → Bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1

            right -= 1

            # 3. Right → Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1

                bottom -= 1

            # 4. Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1

                left += 1

        return matrix