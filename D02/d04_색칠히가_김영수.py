cases = int(input())

for case in range(cases):
    base = [[0 for i in range(10) ]for j in range(10)]
    c = int(input())
    for i in range(c):
        a1, a2, b1, b2, color = map(int, input().split())
        for x in range(a1,b1+1):
            for y in range(a2,b2+1):
                if color == 1:
                    if base[x][y] == 0 or base[x][y] == 1:
                        base[x][y] = color
                    else:
                        base[x][y] = -1
                else:
                    if base[x][y] == 0:
                        base[x][y] = color
                    else:
                        base[x][y] = -1
    cnt = 0
    for i in base:
        cnt += i.count(-1)

    print('#{} {}'.format(case+1,cnt))