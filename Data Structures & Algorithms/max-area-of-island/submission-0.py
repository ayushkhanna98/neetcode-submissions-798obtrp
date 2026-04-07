class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = max(count,self.visitIsland(grid,i,j))
        return count
    
    def visitIsland(self, grid, i,j):
        if not self.inBounds(grid,i,j): 
            return 0

        if grid[i][j] != 1: 
            return 0

        grid[i][j] = -1

        count = 0
        for k in range(1,-2,-2):
            _i = i+k
            _j = j+k

            count+=self.visitIsland(grid,_i,j)
            count+=self.visitIsland(grid,i,_j)
        
        return count + 1

    def inBounds(self, grid, i,j)-> bool:
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])



