class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        q1 = deque()
        sett1 = set()
        q2 = deque()
        sett2 = set()

        for i in range(len(grid)):
            q1.append((i,0))
            sett1.add((i,0))

            q2.append((i,len(grid[0])-1))
            sett2.add((i,len(grid[0])-1))
        
        for i in range(len(grid[0])):
            q1.append((0,i))
            sett1.add((0,i))

            q2.append((len(grid)-1, i))
            sett2.add((len(grid)-1, i))

        
        self.performBFS(grid,sett1,q1)
        self.performBFS(grid,sett2,q2)

        print(sett1, sett2)

        ans = []

        for s1 in sett1:
            if s1 in sett2:
                ans.append([s1[0], s1[1]])


        return ans
    







    def performBFS(self, grid, visited, q):

        while q:
            i,j = q.pop()

            for k in range(1,-2,-2):
                _i = i+k
                _j = j+k

                if self.inBounds(grid,_i,j) and (_i,j) not in visited and grid[_i][j]>=grid[i][j]:
                    q.append((_i,j))
                    visited.add((_i,j))

                if self.inBounds(grid,i,_j) and (i,_j) not in visited and grid[i][_j]>=grid[i][j]:
                    q.append((i,_j))
                    visited.add((i,_j))

            
    def inBounds(self,grid,i,j):
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])
        