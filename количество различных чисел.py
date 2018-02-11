s = input().split()
s.sort()
i = 0
a = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        a += 1
print(a)
def diff_num(
        input().split()):
    s, n = set(), 0
    for i in input().split():
        if i not in s:
            s.add(i)
            n += 1
    return n
