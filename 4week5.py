import math
x = int(input())


for i in range(2, int(math.sqrt(x)) + 1):
    if not x % i:
        print(i)
        break
else:
    print(x)
