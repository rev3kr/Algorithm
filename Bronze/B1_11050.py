import math
def execute():
    n, k = map(int, input().split())
    temp = 1
    for i in range(n, n-k, -1):
        temp *= i
    print(temp//math.factorial(k))
execute()