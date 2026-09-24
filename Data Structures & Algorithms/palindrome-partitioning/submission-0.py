class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        # Helper function to check if all strings in a list are palindromes
        def is_all_palindromes(lst):
            for sub in lst:
                if sub != sub[::-1]: # Python string reversal trick
                    return False
            return True

        def dfs(i):
            # Base Case: Reached the end of the string
            if i >= len(s):
                # Check if the fully built subset contains only palindromes
                if is_all_palindromes(subset):
                    res.append(subset.copy())
                return
            
            # Try every possible slice starting from index i
            for j in range(i, len(s)):
                # Blindly add the substring to the path without checking it
                subset.append(s[i:j+1])
                dfs(j + 1)
                subset.pop()
                
        dfs(0)
        return res