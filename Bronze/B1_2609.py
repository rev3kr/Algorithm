import math

def execute():
    a, b = map(int, input().split())
    print(f"{math.gcd(a, b)}\n{math.lcm(a, b)}")

execute()