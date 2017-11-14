a = input().split()
b = int(a[0])
max = b
p = 0
d = len(a)
while d > 0:
    for i in range(len(a)):
        a[i] = int(a[i])
        if a[i] > max:
            max = a[i]
            d -= 1
            p = i
        elif a[i] <= max:
            d -= 1
            max = max
print(max, p)
