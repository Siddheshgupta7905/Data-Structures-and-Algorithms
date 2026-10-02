import math

class Solution:
    def quadraticRoots(self, a, b, c):
        # code here
        D = b*b - 4*a*c
        
        if D < 0:
            return [-1]
            
        root1 = math.floor((-b + math.sqrt(D))/ (2*a))
        root2 = math.floor((-b - math.sqrt(D))/ (2*a))
        
        if root1 < root2:
            root1, root2 = root2, root1
        
        return [root1, root2]
        
        