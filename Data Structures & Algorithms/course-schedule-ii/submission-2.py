class Solution:
    def findOrder(self, numCourses: int, preReq: List[List[int]]) -> List[int]:

        adjList = defaultdict(list)

        for p in preReq:
            a = p[0]
            b = p[1]
            adjList[a].append(b)
        
        l_ret = []
        cache = set()
        for n in range(numCourses):
            l = self.dfs(adjList, n,set(), cache)
            if l is None: return []

            for i in l:
                l_ret.append(i)
        
        return l_ret
        


    def dfs(self, adjList, curr, visited, cache):
        print(curr)
        if curr in visited:

            return None
    
        if curr in cache:
            return []
        
        visited.add(curr)

        nei = adjList[curr]

        l_ret = []

        for n in nei:
            l = self.dfs(adjList, n, visited, cache)
            if l is None: return None
            for i in l:
                l_ret.append(i)
            

        l_ret.append(curr)  
        visited.remove(curr)
        cache.add(curr)
        return l_ret





        