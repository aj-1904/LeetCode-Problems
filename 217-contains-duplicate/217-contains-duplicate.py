class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countDict = dict()
        flag = False
        for i in range(len(nums)):
            if nums[i] in countDict:
                countDict[nums[i]] += 1
                flag = True
            else:
                countDict[nums[i]] = 1
        
        return True if flag else False
            
                
        