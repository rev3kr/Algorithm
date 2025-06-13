import sys
input = sys.stdin.readline

def back(row):
    global n, board, tmp

    if row == n:
        tmp += 1
        return
    else:
        for col in range(n):
            if promising(row, col):
                board[row] = col
                back(row+1)
                board[row] = -1
    
def promising(row, col):
    global board
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True

n = int(input())
tmp = 0
board = [0 for _ in range(n)]
back(0)
print(tmp)