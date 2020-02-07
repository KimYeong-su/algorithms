T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())

    list_n = list(map(int,input().split()))
    list_m = list(map(int, input().split()))

    max = 0
    if N < M:
        for i in range(M-N+1):
            sum = 0
            for j in range(len(list_n)):
                sum += list_m[i+j]*list_n[j]
            if max < sum:
                max = sum

    else:
        for i in range(N-M+1):
            sum = 0
            for j in range(len(list_m)):
                sum += list_n[i+j]*list_m[j]
            if max < sum:
                max = sum

    print('#{} {}'.format(tc, max))