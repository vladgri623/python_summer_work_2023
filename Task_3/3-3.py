sentence = str(input())
words_unfiltered = sentence.split()
signs = ['.', ',', '!', '?', ':', ';', '"', chr(39)]
words = []

# removes punctuation from words
for i in words_unfiltered:
    for j in i:
        if j in signs:
            i = i.replace(j, '')
    words.append(i)

# sorts words by length
for j in range(len(words)):
    for i in range(len(words)-1):
        if len(words[i]) > len(words[i+1]):
            words[i], words[i+1] = words[i+1], words[i]

# only prints the longest words
longest = len(words[-1])
print("Longest words: ", end='')
for i in words:
    if len(i) == longest:
        print(i, end=' ')


