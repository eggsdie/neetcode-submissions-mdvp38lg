class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for courses, pre in prerequisites:
            preMap[courses].append(pre)


        cycle, visited = set(), set()
        res = []

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
