class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        time = 0
        fresh = 0

        ROWS = len(grid)
        COlS = len(grid[0])

        for r in range(ROWS):
            for c in range(COlS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:

                    n1 = r + dr
                    n2 = c + dc

                    if n1 < 0 or n2 < 0 or n1 == ROWS or n2 == COlS or grid[n1][n2] != 1:
                        continue
                    grid[n1][n2] = 2
                    queue.append([n1, n2])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


    
