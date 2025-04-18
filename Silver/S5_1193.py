temp = 0
x = int(input())
while x > 0:
    temp += 1
    x -= temp
if temp%2 == 1:
    print("%d/%d" % (1-x, temp+x))
else:
    print("%d/%d" % (temp+x, 1-x))