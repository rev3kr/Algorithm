import statistics
def execute():
    n = int(input())
    if n == 0: print("divide by zero")
    else:
        lst = list(map(int, input().split()))
        mean = statistics.mean(lst)
        ex = sum(lst)/len(lst)
        if ex == 0: print("divide by zero")
        else: print(f'{mean/ex:.2f}')
execute()