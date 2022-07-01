class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sums.append(nums[0])
        sum = nums[0]
        for i in range(1,len(nums)):
            sum = sum + nums[i]
            sums.append(sum)
        return sums
            