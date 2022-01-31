​# Solution
# TC - O(N)
# SC - O(1)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        c1 = len(a)-1
        c2 = len(b)-1
        result = ''
        while c1 >= 0 or c2 >= 0:
            sum = carry
            if c1 >= 0:
                sum += ord(a[c1]) - ord('0')
            if c2 >= 0:
                sum += ord(b[c2]) - ord('0')
            c1 -= 1
            c2 -= 1
            carry = 1 if sum > 1 else 0
            result += str(sum % 2)
        if carry:
            result += str(carry)
        return result[::-1]
