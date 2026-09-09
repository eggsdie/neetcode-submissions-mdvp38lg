class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0

        charSet = set()


        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l+=1
                
            charSet.add(s[i])
            longest = max(longest, i-l+1)

        return longest