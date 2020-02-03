# # 2차원 리스트
#
# # 2행 4열 2차원 리스트
# arr = [[1,2,3,4],[5,6,7,8]]
#
# # 1차원 리스트 초기화
# arr = [0,0,0,0,0]
# arr = [0] * 5
# arr = [i for i in range(2,9) if i%2==0]
# # print(arr)
#
# # 2차원 리스트 초기화
# brr = [[1,2,3],[4,5,6],[7,8,9]]
# brr = [[1,2,3]]*3                  # output = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# brr = [[1,2,3] for _ in range(3)]  # output = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#
# brr = [j for i in range(3) for j in range(2)] # output = [0, 1, 0, 1, 0, 1]
# brr = [[i, j] for i in range(3) for j in range(2)] # output = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
# # print(brr)
#
# # 3 4
# # 0 1 0 0
# # 0 0 0 0
# # 0 0 1 0
#
# # col, row = map(int, input().split())
# # crr = []
# # # 방법 1
# # for i in range(col):
# #     num = list(map(int, input().split()))
# #     crr.append(num)
# # print(crr)
#
# # 방법 2
# # n, m = map(int, input().split())
# # my_list = [list(map(int, input().split())) for _ in range(n)]
# # print(my_list)
#
# # 리스트 순회
# # n*m개의 원소를 빠짐없이 조사하는 방법
# arr = [[1,2,3,4,],[5,6,7,8],[9,10,11,12]]
# print(len(arr))     # 행의 길이
# print(len(arr[0]))  # 열의 길이
#
# #행 우선순회
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j],end=' ')
#     print()
#
# #열 우선순회
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j], end=' ')
#     print()
#
# # 지그재그 순회
# N = len(arr)
# M = len(arr[0])
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M-1-2*j) *(i%2)], end=' ')  # i%2는 행을 구분하기 위한 방법
#     print()

# for i in range(N):
#     if i%2==0:
#         for j in range(M):
#             print(arr[i][j], end=' ')
#     else:
#         for j in range(M-1,-1,-1):
#             print(arr[i][j], end=' ')
#     print()

# 2차원 리스트에서 원하는 데이터의 위치 찾기
# # 3 4
# # 0 1 0 0
# # 0 0 0 0
# # 0 0 1 0

# #방법 1
# # n, m = map(int,input().split())
# # my_list = []
# #
# # for i in range(n):
# #     my_list.append(list(map(int,input().split())))
# # result = []
# #
# # for i in range(n):
# #     for j in range(m):
# #         if my_list[i][j] == 1:
# #             temp = [i, j]
# #             result.append(temp)
# # print(result)

# # 전치 행렬
# arr = [[1,2,3,],[4,5,6],[7,8,9]]
#
# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arr[j][i], arr[i][j] = arr[i][j], arr[j][i]
# for i in range(3):
#     for j in range(3):
#         print(arr[i][j], end=' ')
#     print()

# 2차원 리스트에서 네 방향으로 인접요소를 탐색할때 사용하는 방법
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

dx = [-1,0,1,0] # 상하좌우
dy = [0,1,0,-1]

for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX >=0 and nextX < len(arr) and nextY < len(arr[0]) and nextY >= 0:
                print(arr[nextX][nextY],end =' ')
        print()
        