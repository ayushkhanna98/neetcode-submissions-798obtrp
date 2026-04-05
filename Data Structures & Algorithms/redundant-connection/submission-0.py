class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        connections = set()
        self.detectConnected(-1,1,adjList, connections,set())
        ans = []
        for i in range(len(edges)-1,-1,-1):
            if (edges[i][0],edges[i][1]) in connections:
                return [edges[i][0],edges[i][1]]
        return []


    def detectConnected(self, prev,curr, adjList, connections, visited):
        if curr in visited:
            return (curr, curr)
        
        visited.add(curr)

        neighbours = adjList[curr]

        for n in neighbours:
            if n == prev: continue 

            loopStart, lastElement = self.detectConnected(curr, n, adjList, connections, visited)

            if loopStart and lastElement:
                connections.add((curr, lastElement))
                connections.add((lastElement, curr))
                if curr == loopStart:
                    print("e", loopStart, curr, lastElement)
                    return (None, curr)
                else:
                    return (loopStart, curr) 

        

        return (None, curr)




        