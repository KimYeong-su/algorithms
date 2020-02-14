T = int(input())

for tc in range(1,T+1):
    V, E = map(int,input().split())
    base = [[0 for _ in range(V)]for _ in range(V)]

    for _ in range(E):
        a,b = map(int,input().split())
        base[a-1][b-1]=1

    s, e = map(int,input().split())
    stack = [s]
    result = 0
    while True:
        for i in range(V):
            if base[s-1][i] == 1:
                stack.append(i+1)

        if stack[-1]==e:
            result = 1
            break

        s = stack.pop()

        if len(stack) == 0:
            break
    print("#{} {}".format(tc,result))