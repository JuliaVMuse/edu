n = int(input())
sinonimy = {}
for i in range(n):
    first, second = input().split()
    sinonimy[first] = second
    sinonimy[second] = first
print(sinonimy[input()])
