def main():
    t = int(input())
    lst = [0 for _ in range(101)]
    lst[0:6] = [0, 1, 1, 1, 2, 2]
    for i in range(6, 101):
        lst[i] = lst[i-5] + lst[i-1]
    for i in range(t): print(lst[int(input())])

if __name__ == "__main__":
    main()