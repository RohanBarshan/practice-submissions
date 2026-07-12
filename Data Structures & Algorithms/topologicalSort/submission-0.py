class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
        
        topSort = []
        visit = set()
        path = set()
        def dfs(src, adj, visit, topSort, path):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)

            for neighbor in adj[src]:
                if not dfs(neighbor, adj, visit, topSort, path):
                    return False
            path.remove(src)
            topSort.append(src)
            return True

        for i in range(n):
            if i not in visit:
                if not dfs(i, adj, visit, topSort, path):
                    return []
        topSort.reverse()
        return topSort