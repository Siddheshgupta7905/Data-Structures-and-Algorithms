class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            bit1 = 0
            bit2 = 0

            if i >= 0:
                bit1 = ord(s1[i]) - ord('0')

            if j >= 0:
                bit2 = ord(s2[j]) - ord('0')

            total = bit1 + bit2 + carry

            result = chr((total % 2) + ord('0')) + result
            carry = total // 2

            i -= 1
            j -= 1

        # Remove leading zeros
        while len(result) > 1 and result[0] == '0':
            result = result[1:]

        return result