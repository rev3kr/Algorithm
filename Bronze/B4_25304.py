x = int(input()); n = int(input())
temp = 0
for _ in range(n):
    a, b = map(int, input().split())
    temp += a*b

print("Yes" if x == temp else "No")