class Solution:
    def arrange(self, arr):
        n = len(arr)
        result = []

        for i in range(n):
            result.append(arr[arr[i]])

        for i in range(n):
            arr[i] = result[i]