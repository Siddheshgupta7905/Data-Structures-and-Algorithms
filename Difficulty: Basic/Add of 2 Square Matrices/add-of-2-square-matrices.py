class Solution:
	def addMat(self, a, b):
		# Code here
		for i in range(len(a)):
		    for j in range(len(a)):
		        a[i][j] = a[i][j] + b[i][j]