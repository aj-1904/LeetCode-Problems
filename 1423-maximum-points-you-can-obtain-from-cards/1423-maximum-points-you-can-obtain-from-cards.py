class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
#         This problem is similar to minimum sum subarray of size k. Here we require maximum score.
        '''This makes the thing clear that if we have to pick k cards either from the beginning or end such that their sum is maximum, we have to select a subarray of length size-k whose sum is minimum. So we will find that sum and remove that from the total sum of array elements.'''
        n = len(cardPoints)
        i = 0
        j = 0
        tsum = sum(cardPoints)
        minSum = float('inf')
        currSum = 0
        
        if n == k:
            return tsum
        
        while j < n:
            currSum += cardPoints[j]
            
            # if j-i+1 < k:
            #     j += 1
            # sliding window approach to get subarray of minimum sum of length (size-k)
            if j-i+1 == n-k:
                minSum = min(minSum, currSum)
               # move the window
                currSum = currSum - cardPoints[i]
                i += 1
            j += 1
        return tsum-minSum
            
            
            
                    