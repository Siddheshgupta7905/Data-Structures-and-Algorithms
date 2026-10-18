class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i+nums[i])
        return True