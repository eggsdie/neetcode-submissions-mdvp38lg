class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0

        l, r = 0, len(heights) -1

        while l < r:
            mini = min(heights[l], heights[r])

            total = mini*(r-l)
            most = max(total, most)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return most