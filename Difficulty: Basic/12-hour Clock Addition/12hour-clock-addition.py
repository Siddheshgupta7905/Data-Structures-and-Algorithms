class Solution:
    def clockSum(self, x, y):
        # code here
        result = (x+y)%12
        
        if result == 0:
            return '12'
        else:
            return result