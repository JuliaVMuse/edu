a = input().split()
k = 0
d = len(a)
while d > 0:
    for i in range(len(a)):
        a[i] = int(a[i])
        if a[i] > 0:
            k += 1
            d -= 1
        elif a[i] <= 0:
            d -= 1
            k = k
print(k)
