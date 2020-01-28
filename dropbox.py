cases = int(input())

for case in range(cases):
    N, M = map(int,input().split())
    test = list(map(int, input().split()))
    room = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(test[i]):
            room[i][j] = 1

    max = 0
    for k in range(N):
        if test[k] > 0:
            cnt = 0
            for l in range(k+1,N):
                if room[l][test[k-1]]== 10:
                    cnt += 1
                if max < cnt:
                    max = cnt
    print(max)