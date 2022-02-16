class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        B = []
        square = -1
        for i in range(len(nums)):
            square = nums[i] * nums[i]
            B.append(square)
        B.sort()
        return B