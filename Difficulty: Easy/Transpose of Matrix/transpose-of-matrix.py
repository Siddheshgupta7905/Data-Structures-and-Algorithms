class Solution:
    def transpose(self, mat):
        # code here
        rows = len(mat)
        cols = len(mat[0])
        result = []
        for c in range(cols):
            temp = []
            for r in range(rows):
                 temp.append(mat[r][c])
            result.append(temp)
            
        return result
            
        