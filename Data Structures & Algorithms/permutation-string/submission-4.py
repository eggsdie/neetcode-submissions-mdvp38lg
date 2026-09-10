class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        charSet1 = [0]*26
        charSet2 = [0]*26

        for i in range(len(s1)):
            charSet1[ord(s1[i])-ord('a')] +=1
            charSet2[ord(s2[i])-ord('a')] +=1

        matches = 0

        for i in range(26):
            matches+= (1 if charSet1[i]==charSet2[i] else 0) 

        l =0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            charSet2[index] +=1
            if charSet2[index] == charSet1[index]:
                matches+=1
            elif charSet1[index] == charSet2[index] - 1:
                matches-=1

            index = ord(s2[l]) - ord('a')
            charSet2[index] -=1
            if charSet2[index] == charSet1[index]:
                matches +=1
            elif charSet1[index] == charSet2[index] + 1:
                matches-=1 

            l+=1

        return matches == 26
