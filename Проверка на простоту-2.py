import math
x = int(input())


def IsPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            print("NO")
            break
    else:
        print("YES")


IsPrime(x)
