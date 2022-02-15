class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''Kadanes Algorithm'''
        curr_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        