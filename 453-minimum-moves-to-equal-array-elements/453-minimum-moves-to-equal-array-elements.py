class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        mini = min(nums)
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i]-mini)
        return count
            
        