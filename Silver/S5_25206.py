temp = 0
grade = 0
dic = {"A+": 4.5, "A0": 4,"B+": 3.5, "B0": 3,"C+": 2.5, "C0": 2,"D+": 1.5, "D0": 1, "F": 0}
for _ in range(20):
    _, a, b = map(str, input().split())
    if b == 'P':
        continue
    a = float(a)
    temp += a*dic[b]
    grade += a
print(temp/grade)