n = int(input())
b = 1
temp = 0
while n > 0:
    n = n-b
    if temp == 0:
        b *= 6
    else:
        b += 6
    temp += 1
print(temp)