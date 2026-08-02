class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res