class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        max_heap = []
        tsum = 0
        for ele in target:
            heapq.heappush(max_heap, -ele)
            tsum += ele
            
        while max_heap[0] != -1:
            top = -heapq.heappop(max_heap)
            tsum = tsum - top
            
            if tsum <= 0 or tsum >= top:
                return False
            
            top = top % tsum
            tsum = tsum + top
            heapq.heappush(max_heap, -top or -tsum)
            
        return True
        