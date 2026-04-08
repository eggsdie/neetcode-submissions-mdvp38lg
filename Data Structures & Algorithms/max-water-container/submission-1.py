class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        area = 0

        while l < r:
            curr_width = r-l
            curr_height = min(heights[l], heights[r])
            area = max(curr_width*curr_height, area)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return area
        