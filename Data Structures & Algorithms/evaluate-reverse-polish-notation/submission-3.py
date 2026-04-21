class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a,b = stack.pop(), stack.pop()
                ans = int(float(b/a))
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[0]
        