def execute():
    def merge_sort(A, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort(A, p, q)
            merge_sort(A, q+1, r)
            merge(A, p, q, r)
    
    def merge(A, p, q, r):
        nonlocal temp, check
        tmp = []
        i = p; j = q+1
        while i <= q and j <= r:
            if A[i] <= A[j]:
                tmp.append(A[i]); i += 1
            else:
                tmp.append(A[j]); j += 1
        while i <= q:
            tmp.append(A[i]); i += 1
        while j <= r:
            tmp.append(A[j]); j += 1
        i = p; t = 0
        while i <= r:
            A[i] = tmp[t]
            i += 1; t += 1; temp += 1
            if temp == k:
                check = True
                print(A[i-1])

    a, k = map(int, input().split())
    lst = list(map(int, input().split()))
    temp = 0; check = False
    merge_sort(lst, 0, a-1)
    if not check: print(-1)
execute()