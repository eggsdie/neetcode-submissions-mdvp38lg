class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        inside = set()
        for n in nums:
            if n in inside:
                return True
            else:
                inside.add(n)
        return False
