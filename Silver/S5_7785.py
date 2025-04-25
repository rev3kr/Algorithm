s = set()
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if b == "enter":
        s.add(a)
    else:
        s.discard(a)
s = sorted(list(s), reverse=True)
for i in s:
    print(i)