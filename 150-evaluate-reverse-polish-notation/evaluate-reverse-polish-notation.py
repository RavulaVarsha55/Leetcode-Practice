class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:

            if self.is_number(i):
                stack.append(int(i))
            elif i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                stack.append(stack.pop(-2) - stack.pop(-1))

            elif i == "*":
                stack.append(stack.pop() * stack.pop())


            else:
                stack.append(int(stack.pop(-2)/stack.pop(-1)))

        return stack[-1]
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False
