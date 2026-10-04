class Solution:
    def findDuplicates(self, arr):
        # code here
        freq = {}
        result = []
        
        for num in arr:
            freq[num] = freq.get(num,0)+1
            
        for num in freq:
            if freq[num] > 1:
                result.append(num)
                
        return result