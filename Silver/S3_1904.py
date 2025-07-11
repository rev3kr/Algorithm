def main():
    n = int(input())
    if n == 1: print(1)
    elif n == 2: print(2)
    else:
        num1, num2 = 1, 2
        for i in range(2, n):
            num1, num2 = num2, (num1%15746 + num2%15746) % 15746
        print(num2)

if __name__ == "__main__":
    main()