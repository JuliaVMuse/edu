n = int(input())
pre = input()
res = set()
for i in range(n):
    res.add(i + 1)
while pre != "HELP":
    pre = set(map(int, pre.split()))
    ans = input()
    if ans == "YES":
        res &= pre
    elif ans == "NO":
        res -= pre
    pre = input()
print(*(sorted(res)))
