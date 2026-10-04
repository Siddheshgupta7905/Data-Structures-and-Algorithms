class Solution:
    def sumExceptFirstLast(self,arr):
        # code here
        total = 0
        for i in range(1, len(arr)-1):
            total += arr[i]
        return total