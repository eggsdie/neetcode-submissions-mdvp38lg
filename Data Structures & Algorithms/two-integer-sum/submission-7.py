class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inside = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in inside:
                return [inside[diff], i]

            inside[n] = i

            