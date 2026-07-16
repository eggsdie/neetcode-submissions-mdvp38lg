class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        settings = { ")": "(", "]": "[", "}": "{"
        }

        for c in s:
            if c in settings:
                if stack and stack [-1] == settings[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)


        return True if not stack else False