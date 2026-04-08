class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # al=defaultdict(list)
        # for e in edges:
        #     al[e[0]].append(e[1])
        #     al[e[1]].append(e[0])
        

        # visited = set()

        # ans = self.recurse(-1,0,al,visited)

        # if len(visited) == n:
        #     return ans
        # else:
        #     return False

        dsu = [i for i in range(0,n)]

        for e in edges:
            a = e[0]
            b = e[1]

            if self.findParent(dsu,a) == self.findParent(dsu,b):
                return False
            else:
                self.join(dsu,a,b)
            print(e,dsu)
        
        p = None
        for e in range(n): 
            if p is not None and p!=self.findParent(dsu,e):
                return False

            else:
                p = self.findParent(dsu,e)
        return True
    

    def join(self, dsu, a, b):
        p_a = self.findParent(dsu, a)
        p_b = self.findParent(dsu, b)

        dsu[p_b] = p_a


    def findParent(self, dsu, e)-> int:
        if e != dsu[e]:
            dsu[e] = self.findParent(dsu,dsu[e])
        return dsu[e]

    # def recurse(self, prev,curr, al, visited) -> bool:

        

    
        