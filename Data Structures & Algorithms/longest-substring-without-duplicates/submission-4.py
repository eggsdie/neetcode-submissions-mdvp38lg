class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
                
            maxi = r-l+1
            res = max(res, maxi)
            charSet.add(s[r])

        return res

