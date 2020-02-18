def find(r,c):
    stack = [(r,c)]
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]

    while len(stack)!=0:
        pr,pc = stack.pop()
        for i in range(4):
            nr = pr + dx[i]
            nc = pc + dy[i]
            if 0<=nr<N and 0<=nc<N:
                if base[nr][nc]==0:
                    stack.append((nr,nc))
                    base[nr][nc]=4
                elif base[nr][nc]==3:
                    return 1
    return 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base = [list(map(int,input()))for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if base[i][j]==2:
                s_r, s_c = i, j
                break
    
    print('#{} {}'.format(tc, find(s_r,s_c)))
