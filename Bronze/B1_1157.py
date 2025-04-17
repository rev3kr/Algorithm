s = input().upper()
lst = [0 for _ in range(26)]
for i in s:
    lst[ord(i)-65] += 1
temp = 0
for i in range(26):
    if lst[i] == max(lst): temp += 1
print(chr(lst.index(max(lst))+65) if temp == 1 else '?')