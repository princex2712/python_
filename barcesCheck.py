# Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class Parentheses:
    def is_valid_para(self,str1):
        stack = []
        pchar = {"[":"]","{":"}","(":")"}
        for para in str1:
            if para in pchar:
                stack.append(para)
            elif len(stack)==0 or pchar[stack.pop()]!=para:
                return False
        return len(stack)==0
p = Parentheses()
print(p.is_valid_para("(){}[]"))
print(p.is_valid_para("()[{)}"))
print(p.is_valid_para("()"))