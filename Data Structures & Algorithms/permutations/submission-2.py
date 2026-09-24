class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i+=1

                subset.append(nums[i])
                dfs()
                subset.pop()

        dfs()

        return res
                