cases = int(input())

for case in range(cases):
    base = [1,2,3,4,5,6,7,8,9,10,11,12]
    N, K = map(int, input().split())

    n = len(base)
    result = []
    for i in range(1<<n):
        temp = []
        for j in range(n+1):
            if i & (1<<j):
                temp.append(base[j])
        result.append(temp)

    cnt = 0
    for i in range(len(result)):
        if len(result[i]) == N:
            if sum(result[i]) == K:
                cnt +=1

    print('#{} {}'.format(case+1,cnt))