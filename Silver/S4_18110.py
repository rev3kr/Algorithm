import statistics, math, sys
input = sys.stdin.readline
def execute():
    n = int(input())
    if n == 0:
        print(0)
        return
    floor = math.floor(n*0.15+0.5)
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    lst.sort()
    print(math.floor(statistics.mean(lst[floor:len(lst)-floor])+0.5))
execute()