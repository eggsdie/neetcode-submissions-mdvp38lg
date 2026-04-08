class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""
        for n in strs:
            new += str(len(n)) + "#" + n

        return new
            



    def decode(self, s: str) -> List[str]:
        old, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            old.append(s[j + 1:j+1+length])
            i= j+1+length

        return old

