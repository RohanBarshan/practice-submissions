class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        path = set()

        def dfs(src):
            if src in path:
                return False
            
            if src in visit:
                return True
            
            path.add(src)

            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
                
            path.remove(src)
            visit.add(src)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
