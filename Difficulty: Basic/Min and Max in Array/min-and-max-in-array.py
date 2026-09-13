class Solution:
    def getMinMax(self, arr):
        # code here
        minimum = arr[0]
        maximum = arr[0]

        for num in arr:
            if num < minimum:
                minimum = num

            if num > maximum:
                maximum = num

        return [minimum, maximum]