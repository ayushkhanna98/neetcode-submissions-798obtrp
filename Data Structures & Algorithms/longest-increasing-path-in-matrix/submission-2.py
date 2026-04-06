class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        mapp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(self.getLongest( matrix, i,j,mapp, set()), ans)
        print(mapp)
        return ans

    



    def getLongest(self,matrix, i,j, mapp, visited) -> int:

        if (i,j) in mapp:
            return mapp[(i,j)]


        

        maxLen = 0
        visited.add((i,j))
        for x in range(1,-2,-2):
            i_ = i+x
            j_ = j+x
            if self.inBounds(matrix,i_,j) and matrix[i_][j] > matrix[i][j] and (i_,j) not in visited:
                maxLen = max(self.getLongest(matrix,i_,j,mapp, visited), maxLen)

            if self.inBounds(matrix,i,j_) and matrix[i][j_] > matrix[i][j] and (i,j_) not in visited:
                maxLen = max(self.getLongest(matrix,i,j_, mapp, visited),maxLen)
        
        if (i,j) in mapp:
            mapp[(i,j)] = max(maxLen + 1, mapp[(i,j)])
        else:
            mapp[(i,j)] = maxLen + 1
        visited.remove((i,j))

        return maxLen + 1


    def inBounds(self, m, i ,j):
        return i>=0 and i<len(m) and j>=0 and j<len(m[0])
        