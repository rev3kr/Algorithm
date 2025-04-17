s = input()
lst = [-1 for _ in range(26)]
for i in s:
    lst[ord(i)-97] = s.index(i)
print(*lst)