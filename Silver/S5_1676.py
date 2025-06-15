import math
def execute():
    n = int(input())
    s = str(math.factorial(n))
    for i in range(-1, -1*len(s), -1):
        if s[i] != "0":
            print((i+1)*-1)
            return
    print(0)
execute()