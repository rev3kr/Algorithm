lst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
for i in lst:
    s = s.replace(i, '#')
print(len(s))