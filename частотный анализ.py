inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read().split()
counter = {}
words = []
for word in lines:
    words.append(word)
words.sort()
for word in words:
    counter[word] = counter.get(word, 0) + 1
a = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
for i in a:
    print(i[0])
inFile.close()
