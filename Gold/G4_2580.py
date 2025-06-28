def execute():
    def back(n):
        nonlocal sudoku, blank

        if n == len(blank):
            for i in sudoku:
                print(*i)
            exit()
        else:
            for num in range(1, 10):
                x, y = blank[n]
                if check(x, y, num):
                    sudoku[x][y] = num
                    back(n+1)
                    sudoku[x][y] = 0
    
    def check(x, y, num):
        for i in range(9):
            if sudoku[x][i] == num or sudoku[i][y] == num:
                return False

        for i in range(3):
            for j in range(3):
                if sudoku[x//3 * 3 + i][y//3 * 3 + j] == num:
                    return False
        return True
    
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    blank = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    back(0)
execute()