inFile = open('input4', 'r', encoding='utf8')
lines = inFile.readlines()
num_votes = {}
for line in lines:
    print(line)
    candidate, votes = line.split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)
for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
inFile.close()
