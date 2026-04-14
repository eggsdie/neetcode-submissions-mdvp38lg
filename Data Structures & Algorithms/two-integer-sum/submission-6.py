class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            req = target-n
            if req in prev:
                return [prev[req], i]

            prev[n] = i