"""
Write a Python program to get all strobogrammatic numbers that are of length n.
A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).

"""
def fun(n):
    bases = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    def generate(num):
        if len(num) == n:
            return [num]
        result = []
        for key in bases:
            if n != 1 and key == '0':
                continue
            result.extend(generate(key + num + bases[key]))
        return result
    if n % 2 == 0:
        return generate('')
    else:
        return generate('0'), generate('1'), generate('8')
print("n = 2: \n", fun(2))
print("n = 3: \n", fun(3))
print("n = 4: \n", fun(4))