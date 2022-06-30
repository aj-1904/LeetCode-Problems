class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i]-nums[mid])
            
        return count
            
            
        