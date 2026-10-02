class Solution:
    def sortedMatrix(self, mat):
        # code here
        n = len(mat)
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append(mat[i][j])
                
        arr.sort()
        
        index = 0
        for i in range(n):
            for j in range(n):
                mat[i][j] = arr[index]
                index+=1
                
        return mat