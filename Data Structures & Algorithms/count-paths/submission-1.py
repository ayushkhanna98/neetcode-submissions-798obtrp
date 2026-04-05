class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[0] * n for _ in range(m)]
        for r in grid: r[0] = 1
        for i in range(len(grid[0])): grid[0][i] = 1


        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]

        