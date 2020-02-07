T=int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]

    cnt=0

    for i in range(N):              # 가로 방향 검사
        words = 0   # 빈칸수
        cur = 0     # 현재 위치
        while cur < N:
            if puzzle[i][cur] == 1: # 검사 위치가 1일때
                words +=1
                if words == K and cur == N-1:
                    cnt += 1
            else:                   # 검사 위치가 0일때
                if words == K:
                    cnt +=1
                words = 0
            cur += 1

    for j in range(N):              # 세로 방향 검사
        words = 0   # 빈칸수
        cur = 0     # 현재 위치
        while cur < N:
            if puzzle[cur][j] == 1: # 검사 위치가 1일때
                words +=1
                if words == K and cur == N-1:
                    cnt += 1
            else:                   # 검사 위치가 0일때
                if words == K:
                    cnt +=1
                words = 0
            cur += 1

    print('#{} {}'.format(tc, cnt))