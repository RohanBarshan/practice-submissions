class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visited = set()
        visiting = set()

        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False
            visiting.add(src)

            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            visiting.remove(src)
            visited.add(src)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
