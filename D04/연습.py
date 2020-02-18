
# 가위:1 바위:2 보:3
def tornement(a,i,j):
    pivot = (i+j)//2
    L = i
    R = j
    while L < R:
        if a[piovt]!=3:
            while(a[L]<a[pivot] and L<R) : L+=1
            while(a[R]>=a[pivot] and L<R) : R+=1
        else:
            
        if L < R :
            if L==pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base = list(map(int,input().split()))
    print(tornement(base,0,N-1))

    # print('#{} {}'.format(tc,base[0]))
