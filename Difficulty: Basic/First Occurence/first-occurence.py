class Solution:
    def firstOccurence(self, txt: str, pat: str) -> int:
        n, m = len(txt), len(pat)

        # Loop through txt where pat could potentially fit
        for i in range(n - m + 1):
            if txt[i:i+m] == pat:
                return i

        return -1
