class Solution:
    def minDeletions(self, s: str) -> int:
        
        countMap = {}
        uniquelst = []
        count = 0
        
        '''store the frequency of each character in dictionary'''
        for i in range(len(s)):
            if s[i] in countMap:
                countMap[s[i]] += 1
            else:
                countMap[s[i]] = 1
        
        '''If similar value already present then decrement  '''
        for value in countMap.values():
            while value > 0 and value in uniquelst:
                count += 1
                value -= 1
            if value not in uniquelst:
                uniquelst.append(value)
        return count
                
                
        
        
        
        