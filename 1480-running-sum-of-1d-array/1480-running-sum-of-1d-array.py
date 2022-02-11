class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = 0
        running_sum = []
        for i in range(len(nums)):
            rsum += nums[i]
            running_sum.append(rsum)
        return running_sum