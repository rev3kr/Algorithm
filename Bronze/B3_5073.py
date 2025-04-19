while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0: break
    lst.sort()

    if lst[2] >= sum(lst[0:2]): print("Invalid")
    elif lst[0] == lst[1] == lst[2]: print("Equilateral")
    elif lst[0] == lst[1] or lst[1] ==lst[2]: print("Isosceles")
    else: print("Scalene")