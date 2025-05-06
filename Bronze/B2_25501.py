temp = 0
def recursion(s, l ,r):
    global temp
    temp += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global temp
    temp = 0
    return recursion(s, 0, len(s)-1)

def execute():
    n = int(input())
    for _ in range(n):
        s = input()
        print(f'{isPalindrome(s)} {temp}')
execute()