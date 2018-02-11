inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read().split()
words = dict()
word = []
for i in lines:
        words[i] = t = words.get(i, 0) + 1
        word.append(words[i]-1)
print(*word)
inFile.close()
