def execute():
    n = int(input())
    qsList = list(map(int, input().split()))
    qsNum = list(map(int, input().split()))
    m = int(input())
    lst = list(map(int, input().split()))
    lst2 = []
    for i in range(n-1, -1, -1):
        if qsList[i] == 0:
            lst2.append(qsNum[i])
            m -= 1
        if m == 0: break
    lst2.extend(lst[:m])
    print(*lst2)

execute()