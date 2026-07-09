class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, e in enumerate(edges):
            e.append(i) #[v1, v2, weight, original index]
        
        edges.sort(key = lambda e: e[2])
        
        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            # Try without curr edge
            weight = 0
            uf_exclude = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf_exclude.union(v1, v2):
                    weight += w
            if uf_exclude.count > 1 or weight > mst_weight:
                critical.append(i)
                continue
            
            # Try with curr edge
            weight = e_weight
            uf_include = UnionFind(n)
            uf_include.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf_include.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        
        return [critical, pseudo]