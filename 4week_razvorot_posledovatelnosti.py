def rec():
    print(a[d-1])


a = []
n = int(input())
while n != 0:
    if n != 0:
        a.append(n)
        n = int(input())
a.append(0)
d = len(a)
while d > 0:
    rec()
    d -= 1
