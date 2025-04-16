n = int(input())
temp = ""
for i in range(1, n+1):
    temp += " " * (n-i) + "*" * i + "\n"
print(temp)