class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight):
                return

            visit.add((r, c))

            dfs(r, c, visit, heights[r][c])
            dfs(r, c, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[r][c])
            dfs(rows-1, c, atl, heights[rows-1][c])