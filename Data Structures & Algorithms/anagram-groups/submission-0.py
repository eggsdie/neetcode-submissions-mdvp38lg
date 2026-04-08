class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            values[sortedS].append(s)

        return list(values.values())

        