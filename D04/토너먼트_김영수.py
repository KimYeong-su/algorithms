# 가위:1 바위:2 보:3
def tournament(p,i,j):
    if len(p)==1:
        return p[0]

    a = tournament(p,i,(i+j)//2)
    b = tournament(p,(i+j)//2+1,j)
    if base[a] == 1:
        if base[b] == 1:
            return a
        elif base[b] == 2:
            return b
        else:
            return a
    elif base[a] == 2:
        if base[b] == 2:
            return a
        elif base[b] == 3:
            return b
        else:
            return a
    elif base[a] == 3:
        if base[b] == 3:
            return a
        elif base[b] == 1:
            return b
        else:
            return a
    

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base = list(map(int,input().split()))
    base_index = [i for i in range(N)]
    print(tournament(base_index,0,N-1))

    # print('#{} {}'.format(tc,base[0]))