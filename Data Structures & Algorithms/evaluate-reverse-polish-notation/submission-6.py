class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n =="+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif n== "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif n=="/":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b / a))
            elif n=="-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b)-int(a))
            else:
                stack.append(int(n))

        return stack[-1]
