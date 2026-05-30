
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue  = deque()
        res = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            level = []

            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)
                
        return res