class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = []

        def dfs(i):
            if i == len(nums):
                res.append(counter.copy())
                return 
            counter.append(nums[i])
            dfs(i+1)
            counter.pop()
            dfs(i+1)

        
        dfs(0)

        return res
            

            