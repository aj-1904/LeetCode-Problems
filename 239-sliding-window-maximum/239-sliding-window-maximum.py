from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = [] 
        queue = deque()
        
        for i in range(0, k):
            
            while queue and queue[-1] < nums[i]:
                queue.pop()
        
            queue.append(nums[i])
        output.append(queue[0])
            
        for i in range(k, n):
            
            if queue[0] == nums[i-k]:
                queue.popleft()
            
            while queue and queue[-1] < nums[i]:
                queue.pop()
        
            queue.append(nums[i])
            output.append(queue[0])
    
        return output
        