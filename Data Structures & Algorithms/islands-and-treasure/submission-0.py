class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))


        while q:
            r, c = q.popleft()
            inf = 2147483647
            for dr, dc in directions:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[dr + r][dc+c] == inf:
                    grid[dr+r][dc+c] = grid[r][c] + 1
                    q.append((dr+r, dc+c))



                