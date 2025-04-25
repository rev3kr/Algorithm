n, m = map(int, input().split())
s1 = set([input() for _ in range(n)])
s2 = set([input() for _ in range(m)])
common = sorted(list(s1 & s2))
print(len(common))
for i in common:
    print(i)