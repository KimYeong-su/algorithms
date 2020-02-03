# 연습문제1
# 2 7 4 3 6
# 8 5 8 3 2
# 2 2 3 6 9
# 5 9 2 5 7
# 3 6 2 9 4

arr = [list(map(int, input().split())) for _ in range(5)]
# print(arr)
dr = [-1,0,1,0] # 델타인덱스
dc = [0, 1, 0, -1]
sum = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr < 0 or nr > len(arr)-1 or nc < 0 or nc > len(arr[0])-1:
                continue
            sum = sum + abs(arr[i][j]-arr[nr][nc])
        print(sum, end=' ')
    print()