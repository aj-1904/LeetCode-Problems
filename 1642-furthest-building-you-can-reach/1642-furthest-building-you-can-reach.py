class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        diff = 0
        heap = []
        bricksUsed = 0
        
        for i in range(1,n):
            diff = heights[i] - heights[i-1]
            '''Calculating the difference between consecutive heights of buildings...
                if Difference less than zero then we will ignore otherwise
                we will do some operation with min heap...'''
            
            if diff > 0:
                heapq.heappush(heap, diff)
            # if ladder is less than heap then we will use brick which is at the top of min                 heap...
                if ladders < len(heap):
                    bricksUsed += heapq.heappop(heap)
            #  if bricksused is more than number of bricksthen we will return that position.. it means we cant go any further with ladders or bricks                
                if bricksUsed > bricks:
                    return i-1
        return n-1
                
            
        