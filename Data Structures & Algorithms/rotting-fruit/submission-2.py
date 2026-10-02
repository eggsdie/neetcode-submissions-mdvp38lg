class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = 0
        q = deque()
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r, c))



        while q:#and fresh but I want to test something
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[dr +r][dc+c] == 1:
                        grid[r+dr][c+dc] = 2
                        fresh-=1
                        q.append((r+dr, c+dc))

            res+=1


        return res -1 if fresh==0 else -1
