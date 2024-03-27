# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
def fun(sequence):
    line = []
    if sequence:
        line.append(sequence.lower())
    return line
print(fun('W3RESource'))