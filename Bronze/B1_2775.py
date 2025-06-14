from itertools import accumulate
def execute():
    lst = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(15):
        lst[0][i] = i
    
    for j in range(1, 15):
        for i in range(15):
            lst[j] = list(accumulate(lst[j-1]))

    t = int(input())
    for _ in range(t):
        k = int(input()); n = int(input())
        print(lst[k][n])

execute()