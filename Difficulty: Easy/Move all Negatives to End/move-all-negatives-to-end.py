class Solution:
    def segregateElements(self, arr):
        positive = []
        negative = []

        for num in arr:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        index = 0

        for num in positive:
            arr[index] = num
            index += 1

        for num in negative:
            arr[index] = num
            index += 1