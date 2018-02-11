inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
counter = {}
names = []
sim = str("\n")
for name in lines:
    if name[-1] == '\n':
        names.append(name[:-1])
    else:
        names.append(name)
    name = lines
names.sort()
inFile.close()
for word in names:
    counter[word] = counter.get(word, 0) + 1
a = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
if int(a[0][1]) > int(len(lines) * 1/2):
    print(a[0][0], file=outFile)
else:
    print(a[0][0], '\n', a[1][0], file=outFile)
outFile.close()
