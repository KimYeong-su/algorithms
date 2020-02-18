T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    cnt = 0
    for c in range(N):          # 세로 방향으로 자성 (열단위로 작업)
        obstacle = 0            # 방해물 수 체크하기
        for r in arr[r][c]==0:
            continue
        elif arr[r][c] == 2 and obstacle==0:
            continue
        elif arr[r][c] == 2 and obstacle!=0:
            cnt +=1
            obstacle=0
        elif arr[r][c] == 1:
            obstacle=1
    print('#{} {}'.format(tc,cnt))