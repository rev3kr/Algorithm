import statistics, sys, math
input = sys.stdin.readline
def execute():
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    mean = statistics.mean(lst)
    print(int(mean + 0.5) if mean >= 0 else int(mean - 0.5))
    print(statistics.median(lst))
    mode = sorted(statistics.multimode(lst))
    print(mode[0] if len(mode) == 1 else mode[1])
    print(max(lst) - min(lst))
execute()