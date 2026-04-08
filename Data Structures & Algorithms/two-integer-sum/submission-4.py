class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inside = {}

        for i, n in enumerate(nums):
            if (target-n) in inside:
                return [inside[target -n], i]

            inside[n]= i