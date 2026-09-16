class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	left = 0
    	for right in range(len(arr)):
    	    if arr[right] != 0:
    	        arr[left], arr[right] = arr[right],arr[left]
    	        left+=1
    	        