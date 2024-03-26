"""
 Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

"""
def generate_strings(letters, used, current_string, all_strings):
    if len(current_string) == len(letters):
        all_strings.append(current_string)
        return

    for i in range(len(letters)):
        if not used[i]:
            used[i] = True
            generate_strings(letters, used, current_string + letters[i], all_strings)
            used[i] = False

def generate_all_strings():
    letters = ['a', 'e', 'i', 'o']
    all_strings = []
    used = [False] * len(letters)
    generate_strings(letters, used, '', all_strings)
    return all_strings

print(generate_all_strings())
