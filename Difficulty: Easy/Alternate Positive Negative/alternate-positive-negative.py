class Solution:
    def rearrange(self, arr):
        positive = []
        negative = []

        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        result = []
        i = j = 0

        while i < len(positive) and j < len(negative):
            result.append(positive[i])
            i += 1

            result.append(negative[j])
            j += 1

        while i < len(positive):
            result.append(positive[i])
            i += 1

        while j < len(negative):
            result.append(negative[j])
            j += 1

        for i in range(len(arr)):
            arr[i] = result[i]