# T = int(input())
#
# for tc in range(1,T+1):
#     N, M = map(int,input().split())
#     base = [list(map(int,input().split())) for _ in range(N)]
#
#     max = 0
#     for i in range(N):
#         for j in range(M):
#             p = base[i][j]
#             temp = p
#             for k in range(1,p+1):
#                 if i-k>=0:
#                     temp += base[i-k][j]
#                 if i+k<N:
#                     temp += base[i+k][j]
#                 if j-k>=0:
#                     temp += base[i][j-k]
#                 if j+k<M:
#                     temp += base[i][j+k]
#             if max<temp:
#                 max = temp
#     print('#{} {}'.format(tc,max))

# 위 오른 아래 왼 : 변화량(델타)
di = [-1,0,1,0]
dj = [0,1,0,-1]

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    for i in range(N):
        for j in range(M):
            k = arr[i][j];
            sum = k
            for d in range(4): # 탐색 방향 정하기
                ni, nj = i+di[d], j+dj[d]
                h = 1
                while 0<=ni<N and 0<=nj<M and h<=k:
                    sum += arr[ni][nj]  #새로운 좌표의 값 누적하기
                    h+=1
                    ni = ni + di[d] # 지정된 방향으로 좌표 갱신
                    nj = nj + dj[d]
            if maxV < sum:
                maxV = sum
    print('#{] {}'.format(tc,maxV))