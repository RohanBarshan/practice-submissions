class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS -1] == 1:
            return - 1

        queue = deque()
        visit = set()

        queue.append((0,0))
        visit.add((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0,1], [0, -1], [1,0], [-1,0], [1,1], [1,-1],[-1,1], [-1,-1]]

                for dr, dc in neighbors:
                    n1 = r + dr
                    n2 = c + dc
                
                    if n1 < 0 or n2 < 0 or n1 == ROWS or n2 == COLS or ((n1,n2)) in visit or grid[n1][n2] == 1:
                        continue
                    
                    queue.append((n1,n2))
                    visit.add((n1,n2))
            length += 1
        return - 1