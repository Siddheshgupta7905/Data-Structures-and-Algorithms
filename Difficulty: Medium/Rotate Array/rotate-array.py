class Solution:
    def rotateArr(self, arr, d):
        # code here
        n = len(arr)
        d = d % n
        def reverse(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1
                
        reverse(0, d-1)
        reverse(d, n-1)
        reverse(0, n-1)