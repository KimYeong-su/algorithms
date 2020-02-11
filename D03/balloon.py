T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    
    max = 0
    for i in range(N):
        for j in range(M):
            p = base[i][j]
            temp = p
            for k in range(1,p+1):
                if i-k>=0:
                    temp += base[i-k][j]
                if i+k<N:
                    temp += base[i+k][j]
                if j-k>=0:
                    temp += base[i][j-k]
                if j+k<M:
                    temp += base[i][j+k]
            if max<temp:
                max = temp
    print('#{} {}'.format(tc,max))
