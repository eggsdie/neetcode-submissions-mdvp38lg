class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inside = set(nums)
        longest = 0


        for i in range(len(nums)):
            if nums[i]-1 not in inside:
                curr = nums[i]
                total =1
                while curr+1 in inside:
                    total+=1
                    curr+=1
                longest = max(total, longest)
        return longest
