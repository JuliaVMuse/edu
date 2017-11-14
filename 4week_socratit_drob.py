n = int(input())
m = int(input())
p = 0
q = 0
i = 9
while i > 1:
    if n % i == 0 and m % i == 0:
        n = n / i
        m = m / i
        i -= 1
    else:
        i -= 1
p = n
q = m
print(int(p), int(q))
