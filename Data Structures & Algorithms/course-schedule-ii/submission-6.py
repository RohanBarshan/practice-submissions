class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i : [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            pre[crs].append(prereq)
        
        output = []
        visit = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for prereq in pre[crs]:
                if not dfs(prereq):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
