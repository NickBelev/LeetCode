class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                # add the last two accumulated digits on the stack and
                # replace those digits with the evaluated result
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # Correct order for subtraction
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # Correct order for division
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # int() will truncate towards 0
            else:
                stack.append(int(token)) # we encountered a digit, not an operation
        return stack[0] # pop() would work too as the final result
        # should be the simplified value of all the arithmetic op's
