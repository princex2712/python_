word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

dic = {}
for word in sorted(word_list):
    if word[0] not in dic:
        dic[word[0]] = []
    dic[word[0]].append(word)
for letter,words in dic.items():
    print(letter)
    for word in words:
        print(word)