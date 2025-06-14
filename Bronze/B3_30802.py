import math

def execute():
    n = int(input())
    tlist = list(map(int, input().split()))
    plist = list(map(int, input().split()))
    tmp = 0

    for t in tlist:
        if t%plist[0] == 0:
            tmp += t//plist[0]
        else: tmp += t//plist[0] + 1
    print(tmp)
    
    tmp = n//plist[1]
    print(f'{tmp} {n-(tmp*plist[1])}')
execute()