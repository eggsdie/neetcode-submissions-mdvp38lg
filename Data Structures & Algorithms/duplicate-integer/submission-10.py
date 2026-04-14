class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        include = set()

        for n in nums:
            if n in include:
                return True
            include.add(n)

        return False