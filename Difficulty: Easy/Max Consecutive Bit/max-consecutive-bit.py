class Solution:
    def maxConsecBits(self, arr):
        #code here 
        maxCount, count = 0, 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                count+=1
            else:
                maxCount = max(maxCount, count)
                count = 1
        return max(maxCount, count)
            