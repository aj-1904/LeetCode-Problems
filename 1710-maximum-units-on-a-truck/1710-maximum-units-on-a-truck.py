class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        '''Greedy approach
            TC - O(nlogn)
            SC - O(1)'''
        
        # Sort boxes so that boxes with the most units appear first        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        maxUnits = 0
        
        for i in range(len(boxTypes)):
            if truckSize >= boxTypes[i][0]:
                maxUnits += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                continue
                
            else:
                maxUnits += truckSize * boxTypes[i][1]
                break
                
        return maxUnits
            
            
        