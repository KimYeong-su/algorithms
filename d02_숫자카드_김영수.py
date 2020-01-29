cases = int(input())

for case in range(cases):
    N = int(input())
    num = int(input())
    c = [0]*10
    for i in str(num):
        c[10-int(i)-1] += 1

    max = 0
    for k in c:
        if k > max:
            max=k

    print('#{} {} {}'.format(case+1,9-c.index(max),max))