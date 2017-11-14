a = str(input()).split()
b = a[0]
b = int(b)
c = []
for i in range(len(a)):
    b = a[i]
    b = int(b)
    if b > 0:
        c.append(b)
c.sort()
print(c[0])
