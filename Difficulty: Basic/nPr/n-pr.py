class Solution:
    def nPr(self, n: int, r: int) -> int:
        # code here
        
        if r > n:
            return 0
            
        fact_n = 1
        fact_nr = 1
        
        for i in range(1, n + 1):
            fact_n *= i
        
        for i in range(1, n-r+1):
            fact_nr *= i
        
        return fact_n // fact_nr