class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        # code here
        total = 0
        for i in range(1, number+1):
            total += i*i
        return total
            
            