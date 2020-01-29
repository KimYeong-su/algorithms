cases = int(input())

for case in range(cases):
    L, S = map(int, input().split())
    base = list(map(int, input().split()))


    for i in range(L-S+1):
        sum = 0
        for k in range(S):
            sum += base[i + k]
        if i == 0:
            Max = sum
            Min = sum
        if sum > Max:
            Max = sum
        if sum < Min:
            Min = sum

    print('#{} {}'.format(case+1,Max-Min))