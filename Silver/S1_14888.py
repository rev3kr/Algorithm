def execute():
    def back(index, result, add, sub, mul, div):
        nonlocal max_num, min_num
        if index == n:
            max_num = max(max_num, result)
            min_num = min(min_num, result)
            return
        else:
            if add > 0: back(index+1, result+nums[index], add-1, sub, mul, div)
            if sub > 0: back(index+1, result-nums[index], add, sub-1, mul, div)
            if mul > 0: back(index+1, result*nums[index], add, sub, mul-1, div)
            if div > 0:
                if result < 0: back(index+1, -(-result//nums[index]), add, sub, mul, div-1)
                else: back(index+1, result//nums[index], add, sub, mul, div-1)
    n = int(input())
    nums = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    max_num = float('-inf')
    min_num = float('inf')
    back(1, nums[0], add, sub, mul, div)
    print(f"{max_num}\n{min_num}")
execute()