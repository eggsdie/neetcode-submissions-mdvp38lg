class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])

        first = [intervals[0]]

        for start, end in intervals:
            lastEnd = first[-1][1]
            if start <= lastEnd:
                first[-1][1] = max(end, lastEnd)
            else:
                first.append([start, end])


        return first
            