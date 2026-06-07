class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original = image[sr][sc]

        if original == color:
            return image

        
        def dfs(r, c):

            ROWS = len(image) 
            COLS = len(image[0])

            if r < 0 or r == ROWS or c < 0 or c == COLS or image[r][c] != original :
                return

            image[r][c] = color

            dfs(r+1,c)
            dfs(r-1, c)
            dfs(r, c + 1)
            dfs(r, c- 1)
        dfs(sr, sc)
        return image

