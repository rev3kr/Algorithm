def execute():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    glist = [0 for _ in range(n)]
    for i in range(n):
        grade = 1
        for j in range(n):
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                grade += 1
        glist[i] = grade
    print(*glist)

execute()