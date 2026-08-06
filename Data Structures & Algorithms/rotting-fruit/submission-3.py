class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1):
                        continue
                    
                    grid[r][c] = 2
                    q.append([r,c])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else - 1