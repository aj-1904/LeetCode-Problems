class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''1. Use a dictionary to store the sum
            2. Check if sum is == k then increment the count
            3. Check if sum-k is present in dictionary then increment the count by the                      frequency present in hash_table'''
        hash_table = dict()
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                count += 1
            if sum - k in hash_table:
                count += hash_table[sum-k]
            if sum in hash_table:
                hash_table[sum] += 1
            else:
                hash_table[sum] = 1
        return count