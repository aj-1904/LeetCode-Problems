import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        
        '''storing key(first) and arr values(second) as pair in max_heap'''
        for i in range(len(arr)):
            heapq.heappush(max_heap,(-1 * abs(arr[i]-x), -1 * arr[i]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        ans = []
        while max_heap:
            '''we need arr values ans store in ans'''
            value = heapq.heappop(max_heap)
            ans.append(-1 * value[1])
        return sorted(ans)
            
        
        