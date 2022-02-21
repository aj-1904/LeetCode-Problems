class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        i = 0
        j = M - 1
        count = 0
        while i < N and j >= 0:
            if grid[i][j] < 0:
                count += N - i # N-i is negative nos in current column
                j -= 1
            else:
                i += 1
        return count