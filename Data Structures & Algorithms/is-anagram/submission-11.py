class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorteds = {}
        sortedt = {}

        for i in range(len(s)):
            sorteds[s[i]] = 1 + sorteds.get(s[i], 0)
            sortedt[t[i]] = 1 + sortedt.get(t[i], 0)


        return sorteds ==sortedt
