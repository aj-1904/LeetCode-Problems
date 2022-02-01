class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # lsb = take AND of n with 1(lsb)
            lsb = n & 1
            # reverselsb is left shift of lsb
            reverselsb = lsb << (31-i)
            # ans stores the OR with reverselsb
            ans = ans | reverselsb
            # right shift the original no.
            n = n >> 1
        return ans
            
        