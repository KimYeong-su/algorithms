# 부분집합의 합이 10인 경우의 수 구하기
# 완전 탐색
def f(i,N,K):   #i번째 원소를 포함하는 경우/ 포함하지 않은 경우 -> 재귀호출
    global bit
    global cnt
    if i ==N:   #base case : bit의 모든 칸이 결정됨
        s = 0
        for a in range(N):
            if bit[a]==1:
                s += a+1
        if s==K:
            cnt += 1
        return
    else:
        bit[i]=1    # i번째 원소 선택
        f(i+1,N,K)
        bit[i]=0    # i번째 원소 선택 안함
        f(i+1,N,K)

N=10    #원소의 수
K=10    #부분집함의 합
bit = [0]*N #원소의 포함여부 저쟝
cnt = 0 #조건을 만족하는 부분집합의 갯수

f(0,N,K) #부분집합을 구하고 -> 총합이 10인 경우 갯수 구하기
print(cnt)