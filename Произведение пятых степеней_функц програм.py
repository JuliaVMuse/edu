from functools import reduce
print(reduce(lambda a, b: a*(b*b*b*b*b), map(int, input().split()), 1))
