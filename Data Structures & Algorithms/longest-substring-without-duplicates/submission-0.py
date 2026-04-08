class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        total = set()

        for r in range(len(s)):
            while s[r] in total:
                total.remove(s[l])
                l+=1
            total.add(s[r])
            longest = max(longest, r-l+1)


        return longest


            
            
