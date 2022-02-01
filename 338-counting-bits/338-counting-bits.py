class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0]*(n+1)
        for i in range(1,n+1):
            count[i] = count[i//2] + i%2
        return count
        