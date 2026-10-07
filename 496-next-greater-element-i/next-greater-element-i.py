class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hashmap = {}
        result = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                hashmap[smaller] = num
            stack.append(num)

        for num in nums1:
            result.append(hashmap.get(num, -1))

        return result

        