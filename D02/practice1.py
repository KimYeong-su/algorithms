arr= []

# 2 7 4 3 6
# 8 5 8 3 2
# 2 2 3 6 9
# 5 9 2 5 7
# 3 6 2 9 4

for i in range(5):
    arr.append(list(map(int,input().split())))

dx = [-1,0,1,0] # 상하좌우
dy = [0,1,0,-1]

result = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX >=0 and nextX < len(arr) and nextY < len(arr[0]) and nextY >= 0:
                result += abs(arr[x][y] - arr[nextX][nextY])
print(result)
