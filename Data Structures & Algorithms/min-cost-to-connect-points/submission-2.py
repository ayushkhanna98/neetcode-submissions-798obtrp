class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        heap = []

        for i in range(len(points)):
            a = points[i]
            for j in range(i+1,len(points)):
                b = points[j]

                dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
                heapq.heappush(heap,(dist, a,b,i,j))
        ans = 0
        dsu = [i for i in range(len(points))]
        while heap:
            dist, a, b, i,j = heapq.heappop(heap)
            a = tuple(a)
            b = tuple(b)

            if self.isConnected(dsu,i,j): continue
            #if a in connected and b in connected: continue
            # check if can connect



            ans+=dist

            # connected.add(a)
            # connected.add(b)
            # Connect

            self.connect(dsu,i,j)
        return ans
    def isConnected(self, dsu,i,j):
        parenti = self.findParent(dsu,i)
        parentj = self.findParent(dsu,j)

        if parenti==parentj:
            return True
        else:
            return False
    
    def findParent(self, dsu, x):
        if dsu[x] != x:
            dsu[x] = self.findParent(dsu, dsu[x])
        return dsu[x]
    
    def connect(self,dsu,i,j):
        parenti = self.findParent(dsu,i)
        parentj = self.findParent(dsu,j)
        dsu[parenti] = parentj

        



        