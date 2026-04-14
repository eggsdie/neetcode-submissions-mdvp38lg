class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(nums) + 1)]

        for num in nums:
            count[nums] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in (range(freq), -1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if les(res)==k:
                    return res
                    