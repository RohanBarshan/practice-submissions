class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visit = set()
        island = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r == ROW or c == COL or ((r,c)) in visit or grid[r][c] == "0":
                return 0

            visit.add((r,c))

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

        
        for R in range((ROW)):
            for C in range((COL)):
                if grid[R][C] == "1" and ((R,C)) not in visit:
                    island += 1
                    dfs(R,C)
        return island