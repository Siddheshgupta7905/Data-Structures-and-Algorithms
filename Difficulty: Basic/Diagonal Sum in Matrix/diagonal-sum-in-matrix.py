class Solution:
	def diagonalSum(self, mat):
		# Code here
		total = 0
		n = len(mat)
		for i in range(n):
		    total += mat[i][i]
		    total += mat[i][n-i-1]
		return total
		        