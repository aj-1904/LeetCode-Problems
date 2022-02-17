class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[N-1] > nums[N-2]:
            return N-1
        l = 1
        r = N-2
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1