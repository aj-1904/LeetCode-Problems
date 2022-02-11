class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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