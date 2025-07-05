import sys
input = sys.stdin.readline
def execute():
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1: break
        w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
        for i in range(1, 21):
            for j in range(1, 21):
                for k in range(1, 21):
                    if i < j < k:
                        w[i][j][k] = w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
                    else:
                        w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]
        if a <= 0 or b <= 0 or c <= 0: print(f"w({a}, {b}, {c}) = {w[0][0][0]}")
        elif a > 20 or b > 20 or c > 20: print(f"w({a}, {b}, {c}) = {w[20][20][20]}")
        else: print(f"w({a}, {b}, {c}) = {w[a][b][c]}")
execute()