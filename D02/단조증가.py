T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    maxV = -1

    for i in range(len(arr)):
        for j in range(len(arr)):
            num = arr[i] * arr[j]
            if i < j:
                num_copy = num
                pre = 10
                isInc = True
                while num:
                    n= num%10
                    if pre < n:
                        isInc = False
                        break
                    num = num//10
                    pre = n
                if isInc:
                    if maxV < num_copy:
                        maxV = num_copy
    print('#{} {}'.format(tc,maxV))