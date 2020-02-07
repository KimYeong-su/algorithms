def search(r,c):
    # 왼, 오른, 아래 탐색
    dr = [0,0,1]
    dc = [1,-1,0]
    visited = [[0 for i in range(N)] for j in range(N)] # 방문배열 초기화
    num = arr[r][c]
    cnt = 0

    while True:
        if r == 99 : return cnt
        for k in range(3):
            nr = r + dr[k]  # 왼, 오, 아래중 갈수 있는 길 찾기
            nc = c + dc[k]  # 새로운 좌표를 검증하기 위해서 계산

            # 새로운 좌표가 사다리 안인지, 이미 방문했는지, 사다리인지
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if visited[nr][nc] == 1: continue
            if arr[nr][nc] == 0: continue

            # 새로찾은 좌표로 갱신, 방문했다고 표시
            r = nr
            c = nc
            visited[nr][nc] = 1
            num = arr[nr][nc]
            cnt += 1
            break

T = 10
for tc in range(1,T+1):
    t = int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 100*100
    minIdx = 0
    for i in range(N):
        if arr[0][i] == 1:
            # 시작점에서 부터 탐색 시작
            cnt = search(0,i)
            if ans > cnt:
                ans = cnt
                minIdx = i
    print('#{} {}'.format(tc,minIdx))
