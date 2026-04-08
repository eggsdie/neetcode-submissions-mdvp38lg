class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    return True

        return duplicate
        