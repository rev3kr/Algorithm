import math
a, b, v = map(int, input().split())
temp = 0
print(int(math.ceil((v-a)/(a-b)+1)))