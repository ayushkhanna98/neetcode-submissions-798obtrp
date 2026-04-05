# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ansArr = []

        q = deque()
        q.append((root, 0))

        while q:

            node,depth = q.popleft()

            if depth > len(ansArr)-1:
                ansArr.append([node.val])
            else:
                ansArr[depth].append(node.val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

        return ansArr


        