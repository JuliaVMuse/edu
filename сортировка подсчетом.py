mySet = map(int, input().split())
cnt = [0] * 101


def CountSort(mySet):
    for set in mySet:
        cnt[set] += 1
        print(cnt, cnt[set])
    for nowSet in range(len(cnt)):
        print((str(nowSet) + ' ') * cnt[nowSet], end='')


CountSort(mySet)
