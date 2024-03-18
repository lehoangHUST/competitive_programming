class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        stack = []

        # Check number token in stack
        i = 0
        while i < len(tokens):
            if tokens[i] != '-' and tokens[i] != '+' and tokens[i] != '/' and tokens[i] != '*':
                stack.append(tokens[i])
            else:
                print(stack)
                value_1 = int(stack.pop())
                value_2 = int(stack.pop())

                if tokens[i] == '*':
                    r = value_1 * value_2 
                elif tokens[i] == '+':
                    r = value_1 + value_2
                elif tokens[i] == '-':
                    r = value_2 - value_1
                else:
                    r = int(value_2 / value_1)
                stack.append(str(r))

            i += 1
        
        return int(stack[0])
        """

        stack = []
        while len(tokens) > 0:
            toke = tokens.pop(0)
            if toke == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second+first)
            elif toke == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first) # The order of numbers is important
            elif toke == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second*first)
            elif toke == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second)/first)) # evaluates to a 0 with the 6/-132 scenario (as required).
            else:
                stack.append(int(toke))
        return stack.pop()
Console
