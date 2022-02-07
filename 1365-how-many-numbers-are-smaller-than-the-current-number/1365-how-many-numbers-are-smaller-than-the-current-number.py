class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dictionary = dict()
        for i in range(0,len(sorted_nums)):
            if sorted_nums[i] not in dictionary:
                dictionary[sorted_nums[i]] = i
        
        ans = []
        for i in range(len(nums)):
            ans.append(dictionary[nums[i]])
        return ans
            
                
                
            