import math
def execute():
    t = int(input())
    for _ in range(t):
        k, n = map(int, input().split())
        temp = 1
        for i in range(n, n-k, -1):
            temp *= i
        print(temp//math.factorial(k))
execute()