class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited.add((i,j))
        
        ans = 0
        

        while q:
            i,j,time = q.popleft()

            ans = max(ans,time)

            for k in range(1,-2,-2):
                _i = i+k
                _j = j+k

                if self.inBounds(grid,_i,j) and (_i,j) not in visited and grid[_i][j]==1:
                    q.append((_i,j,time+1))
                    visited.add((_i,j))

                if self.inBounds(grid,i,_j) and (i,_j) not in visited and grid[i][_j]==1:
                    q.append((i,_j,time+1))
                    visited.add((i,_j))
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1 and (i,j) not in visited: return -1
        return ans

    


    def inBounds(self,grid,i,j):
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])




