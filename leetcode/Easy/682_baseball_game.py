class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operand = []

        for i, op in enumerate(operations):
            print(i)
            if op == '+':
                operand.append(int(operand[-1] + int(operand[-2])))
            elif op == 'C':
                operand.pop()
            elif op == 'D':
                operand.append(2 * operand[-1])
            else:
                operand.append(int(op))

        return sum(operand)