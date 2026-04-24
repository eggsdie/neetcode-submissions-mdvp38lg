class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        inside = set(nums)

        for n in nums:
            if (n - 1) not in inside:
                length = 0
                while (n + length) in inside:
                    length+=1

                longest = max(longest, length)

        return longest