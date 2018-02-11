myList1 = list(map(int, input().split()))
myList2 = set()
for elem in myList1:
    if elem in myList2:
        print("YES")
        myList2.add(elem)
    else:
        print("NO")
        myList2.add(elem)
