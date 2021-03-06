#s : 선택된 원소들의 합
#r : 남은 원소들의 합(선택가능한 후보중)
def f(i,N,K,s,r):
    global cnt
    #base case
    if s == K:  #나머지 원소 하나라도 더 선택하면 K보다 커짐 -> 더 탐색할 필요 없음
        cnt+=1
        return
    elif i==N:  #모든 원소를 고려했는데 합이 K가 되는 경우가 없음
        if s == K:
            cnt+=1
        return
    elif s>K:   #현재까지의 누적합이 K보다 크면 더 탐색할 필요없음
        return
    elif s+r<K: #현재가지의 합+후보군의 합이 K보다 작다면 정답이 될 가능성 X
        return
    else:
        #i번째 요소가 선택된 경우
        f(i+1,N,K,s+i+1,r-i-1)
        #i번째 요소가 선택되지 않은 경우
        f(i+1,N,K,s,r-i-1)
        #재귀호출
    

N=20    #1부터 N까지가 집합의 원소
K=10    #부분집합의 합
cnt = 0

f(0,N,K,0,(1+N)*N//2)   #원소의 위치(i), 부분집합의 합, 선택후보들의 합
print(cnt)