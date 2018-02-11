inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.read().split()
counter = {}
words = []
for word in lines:
    words = []
    counter[word] = counter.get(word, 0) + 1
    words.append(word)
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
inFile.close()
