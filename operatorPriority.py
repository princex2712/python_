#  Write a Python program to check the priority of the four operators (+, -, *, /).
__priority__ = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
}
def priority(op1,op2):
    return __priority__[op1]>=__priority__[op2]

print(priority('*','-'))
print(priority('+','-'))
print(priority('+','*'))
print(priority('+','/'))
print(priority('*','/'))