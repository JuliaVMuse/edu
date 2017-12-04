inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = sorted(inFile.readlines())
mySet = []
for line in lines:
    s = line.split()
    mySet.append(s[0])
    mySet.append(s[1])
    mySet.append(s[3])
    mySet.append('\n')
print(*mySet, file=outFile)
inFile.close()
outFile.close()
