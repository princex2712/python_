# Write a Python program to convert an integer to a string in any base using recursion 
def to_String(n,base):
    convert_to_str = '0123456789ABCDEF'

    if n < base:
        return convert_to_str[n]
    else:
        return to_String(n//base,base) + convert_to_str [n%base]
print(to_String(2835,16))