class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force - O(n^2)
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # Optimized - Using hashmap - O(n)
        
        dictionary = dict()
        for i in range(len(nums)):
            if target - nums[i] in dictionary:
                return [dictionary[target-nums[i]],i]
            else:
                dictionary[nums[i]] = i
                
            
        
        
        