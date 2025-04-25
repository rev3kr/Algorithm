n, m = map(int, input().split())
s1 = set([input() for _ in range(n)])
s2 = set([input() for _ in range(m)])
common = list(s1 & s2)
common.sort()
print(len(common))
for i in common:
    print(i)