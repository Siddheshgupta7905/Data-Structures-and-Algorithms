class Solution:
    def climbStairs(self, n: int) -> int:

        # Base cases
        if n <= 2:
            return n
        # Fibonacci pattern
        a = 1
        b = 2

        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c

        return b