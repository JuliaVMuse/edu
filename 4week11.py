def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)
    if n % 2 > 0:
        return a * (a ** (n - 1))

a = float(input())
n = float(input())
print(power(a, n))
