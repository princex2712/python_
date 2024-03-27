# Write a Python program to count the number of carry operations for each addition problem.
# According to Wikipedia " In elementary arithmetic, a carry is a digit that is transferred from one column of digits to another column of more significant digits. It is part of the standard algorithm to add numbers together by starting with the rightmost digits and working to the left. For example, when 6 and 7 are added to make 13, the "3" is written to the same column and the "1" is carried to the left".
def fun(x,y):
    carry = 0
    carry_digit = 0
    for i in reversed(range(10)):
        carry_digit = x % 10 + y%10 + carry_digit
        if x==y==0:
            return carry
        if carry_digit > 9:
            carry_digit = 1 
        else:
            carry_digit = 0
        carry+=carry_digit

        x//=10
        y//=10
    return carry
print(fun(786,457))