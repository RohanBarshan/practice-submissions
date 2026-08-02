# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            RightSide = None
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    RightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if RightSide:
                res.append(RightSide.val)
        return res
