x = float(input())
y = float(input())
if x <= 1 and x >= -1 and y <= 1 and y >= -1:
    def IsPointInSquare(x, y):
        return True
    print("YES")
else:
    def IsPointInSquare(x, y):
        return False
    print("NO")
