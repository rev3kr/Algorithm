t = int(input())
for _ in range(t):
    temp = ""
    r, s = map(str, input().split())
    for i in s:
        temp += i*int(r)
    print(temp)