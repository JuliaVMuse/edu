studs = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_every, known_someone = set.intersection(*studs), set.union(*studs)
print(len(known_every), *sorted(known_every), sep='\n')
print(len(known_someone), *sorted(known_someone), sep='\n')
