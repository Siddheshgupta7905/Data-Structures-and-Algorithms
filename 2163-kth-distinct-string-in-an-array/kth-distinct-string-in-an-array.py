class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = {}
        for char in arr:
            freq[char] = freq.get(char, 0) + 1

        for char in arr:
            if freq[char] == 1:
                k-=1
                if k == 0:
                    return char
        return ""
        