cases = int(input())

for case in range(cases):
    p, ta, tb =  map(int, input().split())

    start = 1
    end = p
    cnt_a, cnt_b = 1, 1

    while (start+end)//2 != ta:
        mid = (start+end)//2
        if mid == ta:
            break
        elif mid > ta:
            end = mid
            cnt_a += 1
        else:
            start = mid
            cnt_a += 1

    start = 1
    end = p

    while (start+end)//2 != tb:
        mid = (start+end)//2
        if mid == tb:
            break
        elif mid > tb:
            end = mid
            cnt_b += 1
        else:
            start = mid
            cnt_b += 1

    if cnt_a < cnt_b:
        print('#{} A'.format(case+1))
    elif cnt_a == cnt_b:
        print('#{} 0'.format(case+1))
    else:
        print('#{} B'.format(case+1))