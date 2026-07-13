class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True