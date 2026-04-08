class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        al=defaultdict(list)
        for e in edges:
            al[e[0]].append(e[1])
            al[e[1]].append(e[0])
        

        visited = set()

        ans = self.recurse(-1,0,al,visited)

        if len(visited) == n:
            return ans
        else:
            return False

    def recurse(self, prev,curr, al, visited) -> bool:
        if curr in visited: return False


        nei = al[curr]
        visited.add(curr)

        for n in nei:
            if n!=prev:
                if not self.recurse(curr, n,al,visited):
                    return False
        


        return True
        

    
        