class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = float('-inf')
        second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest and num > second_largest:
                second_largest = num
        
        if second_largest == float('-inf'):
            return -1
        
        return second_largest
                