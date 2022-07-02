class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''TC - O(nlogn)'''
        '''
       1.  max area = max length * max height
       2. The input arrays of cuts can be randomly ordered, but sorting them wouldn't actually   change how the 'cake' is cut
       3. hence, we can sort both arrays, and find the max diff between adjacent elements'''
        mod = 10**9+7
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxWidth = max(horizontalCuts[0], h - horizontalCuts[-1])
        maxLength = max(verticalCuts[0], w- verticalCuts[-1])
        
        for i in range(1, len(horizontalCuts)):
            maxWidth = max(maxWidth, horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1, len(verticalCuts)):
            maxLength = max(maxLength, verticalCuts[i] - verticalCuts[i-1])
            
        return (maxLength * maxWidth) % mod
        