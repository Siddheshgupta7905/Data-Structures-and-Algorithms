class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc  = dec = True
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                inc = False
            if nums[i] < nums[i+1]:
                dec = False
        return inc or dec
        