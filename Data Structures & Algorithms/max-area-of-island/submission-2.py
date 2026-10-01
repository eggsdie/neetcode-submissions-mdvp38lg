class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            value = 1
            for dr, dc in directions:
                value += dfs(dr +r, dc+ c)

            return value


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))


        return res