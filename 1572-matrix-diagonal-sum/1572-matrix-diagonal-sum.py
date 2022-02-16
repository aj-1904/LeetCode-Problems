class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid = n//2
        sum = 0
        for i in range(n):
            sum += mat[i][i]
            sum += mat[n-i-1][i]
        
        if n%2 == 1:
            sum -= mat[mid][mid]
        
        return sum
        