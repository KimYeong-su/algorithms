from itertools import permutations
#세로로 겹치지 않는 배열 합이 조건
#선택가능한 열
#0,1,2
#0,2,1
# => 순열
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base=[list(map(int,input().split()))for _ in range(N)]
    mini = 10000
    for p in permutations(range(N)):
        result = 0
        for i in range(N):
            result += base[i][p[i]]
        if mini>result:
            mini=result

    print('#{} {}'.format(tc,mini))