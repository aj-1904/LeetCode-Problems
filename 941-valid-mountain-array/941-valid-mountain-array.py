class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
    
        if n < 3:
            return False
        if arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False
        
        l = 0
        r = n-1
        
        while l < r:
            if arr[l] < arr[l+1]:
                l += 1
            elif arr[r-1] > arr[r]:
                r -= 1
            else:
                return False
        return True