a = str(input()).split()
b = str(input()).split()
i = 0
j = 0
c = []
while i < len(a) and j < len(b):
    dig1 = a[i]
    dig1 = int(dig1)
    dig2 = b[j]
    dig2 = int(dig2)
    if dig2 <= dig1:
        c.append(b[j])
        j += 1
    else:
        c.append(a[i])
        i += 1
d1 = int(len(a))
d2 = int(len(b))
while i < d1 or j < d2:
    if i < len(a):
        c.append(a[i])
        i += 1
    if j < len(b):
        c.append(b[j])
        j += 1
print(' '.join(map(str, c)))
