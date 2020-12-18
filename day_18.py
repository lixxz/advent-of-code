import sys
import re

puzzle_input = [s.replace(' ', '') for s in sys.stdin.read().split('\n')[:-1]]

def evaluate_part_one(expr):
    expr.reverse()
    operators = []
    operands = []
    idx = 0
    while idx < len(expr):
        if expr[idx] in ['+', '*']:
            operators.append(expr[idx])
        elif expr[idx].isnumeric() :
            operands.append(int(expr[idx]))
        elif expr[idx] == ')':
            operands.append(expr[idx])
        elif expr[idx] == '(':
            while True:
                operand_1 = operands.pop()
                if operand_1 == ')':
                    break
                operand_2 = operands.pop()
                if operand_2 == ')':
                    operands.append(operand_1)
                    break
                # print(operators, operands)
                oper = operators.pop()
                if oper == '+':
                    operands.append(operand_1 + operand_2)
                elif oper == '*':
                    operands.append(operand_1 * operand_2)
        idx += 1
    # print(operators, operands)
    while len(operators) > 0:
        oper = operators.pop()
        if oper == '+':
            t = operands.pop() + operands.pop()
            operands.append(t)
        elif oper == '*':
            t = operands.pop() * operands.pop()
            operands.append(t)
    # print(operators, operands)
    return operands[0]

#part 2
class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Number(self.val * other.val)

    def __mul__(self, other):
        return Number(self.val + other.val)

    def __repr__(self):
        return 'Number(' + str(self.val) + ')'

s = Number(0)
for p in puzzle_input:
    l = ''
    for idx in range(len(p)):
        if p[idx] == '+':
            l += '*'
        elif p[idx] == '*':
            l += '+'
        elif p[idx].isdigit():
            l += str(Number(int(p[idx])))
        else:
            l += p[idx]
    s *= eval(l)

print(s)