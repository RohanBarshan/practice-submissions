class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        def addRooms(r,c):
            if (r < 0 or r >= ROWS or c <0 or c >= COLS or (r,c) in visit or grid[r][c] == -1):
                return 
            
            visit.add((r,c))
            q.append((r,c))
        
        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRooms(r + 1,c)
                addRooms(r - 1,c)
                addRooms(r,c + 1)
                addRooms(r,c - 1)
            dist += 1