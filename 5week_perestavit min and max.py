n = [int(i) for i in input().split()]
data = min(n), max(n)
position = n.index(data[0]), n.index(data[1])
n[position[0]], n[position[1]] = data[1], data[0]
print(' '.join([str(i) for i in n]))
