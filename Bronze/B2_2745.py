n, b = map(str, input().split())
b = int(b)
temp = 0
for i in range(1, len(n)+1):
    if 'A' <= n[i-1] <= 'Z':
        temp += b**(len(n)-i)*(ord(n[i-1])-55)
    else:
        temp += b**(len(n)-i)*(int(n[i-1]))
print(temp)