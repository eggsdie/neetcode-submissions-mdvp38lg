class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        iss = set()

        for n in nums:
            if n in iss:
                return True

            iss.add(n)

        return False