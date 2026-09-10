class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        total = 0

        for c in charSet:

            l = 0
            length = 0
            for r in range(len(s)):
                if s[r] == c:
                    length+=1

                while (r-l + 1 - length) > k:
                    if s[l] == c:
                        length -=1
                    l+=1

                total = max(total, r-l + 1)

        return total
