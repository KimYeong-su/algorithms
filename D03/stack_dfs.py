'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
'''
스택을 활용한 dfs 구현
    방문배열, 스택준비
    
    시작점을 스택에 넣고 방문표시
    스택이 빌때까지 반복
        스택에선 정점을 꺼내옴
        출력
        꺼내온 정점에 인접하고 아직 방문하지 않은 정점을 스택에 넣기
        스택에 넣은 정점을 방문 표시
'''
def dfs(n,V):
    visited = [0 for _ in range(V+1)]       # 방문표시용 배열
    stack = [0 for _ in range(V)]           # 스택
    top = -1                                # top표시

    top +=1
    stack[top] = n      # 시작점을 스택에 넣고 방문했다고 표시
    visited[n] = 1

    while top>=0:
        n = stack[top]  # 스택에서 하나 꺼내오기
        top -= 1
        print(n, end=' ')
        for i in range(1,V+1):
            if adj[n][i]==1 and visited[i]==0:
                top+=1
                stack[top] = i
                visited[i] = 1

V,E = map(int,input().split())
adj = [[0 for _ in range(V+1)]for _ in range(V+1)]
edge = list(map(int,input().split()))
for i in range(E):
    n1, n2 = edge[i*2],edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
for row in adj:
    print(row)
dfs(1,V)        # 시작점, 정점갯수