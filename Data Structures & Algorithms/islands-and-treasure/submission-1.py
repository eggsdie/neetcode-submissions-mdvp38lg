class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[1])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        

        while q:
            r, c = q.popleft()
            inf = 2147483647

            for dr, dc in directions:
                if (r+dr) < rows and (c+dc) >=0 and (c+dc) < cols and grid[r+dr][c+dc] == inf and (r+dr)>= 0:
                    grid[r+dr][c+dc] = grid[r][c] + 1
                    q.append((r+dr, c+dc))

        
