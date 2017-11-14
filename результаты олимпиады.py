class Man:
    name = ''
    height = 0


def manKey(man):
    return (-man.height, man.name)


n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.height = int(tempManData[1])
    man.name = tempManData[0]
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.name)
