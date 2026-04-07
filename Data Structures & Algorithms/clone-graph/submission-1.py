"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        mapp = {}
        visited = set()
        q = deque()

        q.append(node)

        newNode = Node(node.val)
        mapp[node.val] = newNode
        newHead = newNode
        visited.add(node)

        

        while q:

            oldNode = q.popleft()
            newNode = mapp[oldNode.val]

            
            for oldNeighbor in oldNode.neighbors:

                if oldNeighbor.val in mapp:
                    newNode.neighbors.append(mapp[oldNeighbor.val])
                else:
                    newNie = Node(oldNeighbor.val)
                    mapp[newNie.val] = newNie
                    newNode.neighbors.append(mapp[newNie.val])
                    
                
                if oldNeighbor not in visited:
                    q.append(oldNeighbor)
                    visited.add(oldNeighbor)
        
        return newHead








        