import sys
input = sys.stdin.readline
def execute():
    n = int(input())
    string = ""
    stack = []
    num = temp = float('inf')
    for i in range(1, n+1):
        value = int(input())
        if i == 1:
            for j in range(1, value+1):
                stack.append(j)
                string += "+"
            num = value
        if value > num:
            for j in range(num+1, value+1):
                stack.append(j)
                string += "+"
            num = value
        if value <= num:
            temp = stack.pop()
            string += "-"
            if temp != value:
                print("NO")
                return
    print('\n'.join(string))
execute()