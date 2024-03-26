def fun(string):
    words = string.split(' ')
    dictionary = {}

    for word in words:
        clean_word = word.strip('.,!')
        if clean_word in dictionary:
            dictionary[clean_word]+=1
        else:
            dictionary[clean_word]=1
    return dictionary
long_text = "This is a sample long text. It contains multiple words and it repeats some words for demonstration purposes. We will convert this text into a list of words and then count the frequency of each word."
for k,v in fun(long_text).items():
    print(f'{k}:{v}')