class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            sumCandies = candies[i] + extraCandies
            if sumCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
            
        