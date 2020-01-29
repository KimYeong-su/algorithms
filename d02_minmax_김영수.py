cases = int(input())

for case in range(cases):
    N = int(input())
    base = list(map(int, input().split()))
    while N > 0:
        for i in range(N-1):
            if base[i] > base[i+1]:
                base[i], base[i+1] = base[i+1], base[i]
        N -= 1

    result = base[len(base)-1] - base[0]
    print('#{} {}'.format(case+1,result))