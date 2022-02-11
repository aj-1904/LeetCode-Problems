class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(n):
            ans[i] = nums[i]
        for j in range(n):
            ans[j+n] = nums[j]
        return ans
        