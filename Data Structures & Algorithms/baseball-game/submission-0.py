class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for op in operations:
        
            if op == "C" and stack:
                stack.pop()
            elif op == "+" and len(stack) > 1:
                first = stack[-1]
                second = stack[-2]
                stack.append(first + second)
            elif op == "D" and len(stack) >= 1:
                first = stack[-1]
                stack.append(first * 2)
            else:
                 stack.append(int(op))
        return sum(stack)

            

        