class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.performBFS(grid,i,j)
    


    def performBFS(self, grid, i, j):

        q = deque()
        q.append((i,j,0))
        visited = set()
        visited.add((i,j))


        while q:
            i,j,currDist = q.popleft()

            grid[i][j] = min(grid[i][j], currDist)

            for k in range(1,-2,-2):
                _i = i+k
                _j = j+k

                if self.inBounds(_i, j, grid) and (_i,j) not in visited and grid[_i][j]>0:
                    q.append((_i,j,currDist+1))
                    visited.add((_i,j))
                if self.inBounds(i, _j, grid) and (i,_j) not in visited and grid[i][_j]>0:
                    q.append((i,_j,currDist+1))
                    visited.add((i,_j))


    


    def inBounds(self, i,j,grid):
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])




        