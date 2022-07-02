class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''TC - O(nlogn)'''
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
        