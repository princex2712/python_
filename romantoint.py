#  Write a Python class to convert a Roman numeral to an integer.
class Converter:
    def roman_to_int(self,roman_num):
        roman_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int_val = 0
        for i in range(len(roman_num)):
            if i > 0 and roman_val[roman_num[i]] > roman_val[roman_num[i-1]]:
                int_val+=roman_val[roman_num[i]] - 2 * roman_val[roman_num[i-1]]
            else:
                int_val+=roman_val[roman_num[i]]
        return int_val
c1 = Converter()
print(c1.roman_to_int('MMMMIV'))
