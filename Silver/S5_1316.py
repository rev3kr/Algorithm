n = int(input())
temp = n
for _ in range(n):
    lst = [-1 for _ in range(26)]
    s = input()
    lst[ord(s[0])-97] = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            continue
        else:
            if lst[ord(s[i])-97] != -1:
                temp -= 1
                break
            else:
                lst[ord(s[i])-97] = 0
print(temp)