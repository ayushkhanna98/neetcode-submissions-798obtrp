class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.visitIsland(grid,i,j)
                    count+=1
        return count
    




    def visitIsland(self, grid, i,j):
        if not self.inBounds(grid,i,j): return

        if grid[i][j] != '1': return 

        grid[i][j] = '-1'

        for k in range(1,-2,-2):
            _i = i+k
            _j = j+k

            self.visitIsland(grid,_i,j)
            self.visitIsland(grid,i,_j)

    



    def inBounds(self, grid, i,j)-> bool:
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])
        