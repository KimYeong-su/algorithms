def rotate():
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            temp[j][N-i-1] = arr[i][j]  # 90도 회전
    for i in range(N):
        result[i].append(temp[i])
    arr = temp

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = []
    rotate()    #90도
    rotate()    #180도
    rotate()    #270도
    print('#{}'.format(tc))
    for i in range(len(len(result))):
        for j in range(len(result[i])):
            print(''.join(list(map(str,result[i][j]))),end=' ')
        print()