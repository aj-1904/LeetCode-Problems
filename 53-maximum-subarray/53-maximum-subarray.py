class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''kadane's algorithm'''
        
        currSum = 0
        maxSum = float('-inf')
        
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum