string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = ''
n, b = map(int, input().split())
if n == 0: s = '0'
else:
    while n > 0:
        n, r = divmod(n, b)
        s = string[r] + s
print(s)