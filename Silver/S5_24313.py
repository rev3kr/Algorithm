a1, a0 = map(int, input().split())
c = int(input()); n0 = int(input())

if a1 > c: print(0)
elif (a1 - c) * n0 + a0 > 0: print(0)
else: print(1)