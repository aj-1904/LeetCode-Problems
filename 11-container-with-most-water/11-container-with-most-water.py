class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer approach
        maxi, mini = 0,0
        distance = 0
        i, j = 0, len(height) -1
        
        while i < j:
            distance = j-i
            mini = min(height[i], height[j])
            ans = distance * mini
            maxi = max(ans, maxi)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi
        
        