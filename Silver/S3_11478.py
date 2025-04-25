s = input()
se = set()
for i in range(len(s)):
    for j in range(i, len(s)+1):
        se.add(s[i:j])
print(len(se)-1)