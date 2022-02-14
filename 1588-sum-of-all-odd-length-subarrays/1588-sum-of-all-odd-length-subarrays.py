class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        n = len(arr)
        for i in range(n):
            start = n - i
            end = i + 1
            total = start * end
            odd = total // 2
            if total % 2 == 1:
                odd += 1
            result += odd * arr[i]
        return result
        