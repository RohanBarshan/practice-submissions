class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        queue = deque()

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        queue.append((0,0))
        visit.add((0,0))

        length  = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                if r == ROWS - 1 and c == COLS -1:
                    return length
                
                neighbors = [[0,1], [0,-1], [1, 0], [-1, 0], [1,1], [1,-1], [-1,1], [-1,-1]]

                for dr, dc in neighbors:
                    if not (0 <= r + dr < ROWS and 0 <= c + dc < COLS) or (r + dr, c + dc) in visit or grid[r+dr][c+dc] == 1:
                        continue
                    
                    queue.append((r+dr, c + dc))
                    visit.add((r+dr, c + dc))
            length += 1
        return -1