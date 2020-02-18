#분할정복
#큰 문제를 해결할 수 있는 작은 문제로 분할하여 정복해 나가는 기법
#카드가 한장 될때까지 나눔
    #find() : 각 토너먼트에서 이긴 카드에 대해서 승부하기
    #카드가 한장될때까지 나눔 -> 재귀호출

def find(i,j):      # i : 시작점, j : 끝점 => 카드리스트 범위
    if i==j:        # 카드가 한장일때
        return i
    else:           # 그렇지 않으면
        result1 = find(i,(i+j)//2)
        result2 = find((i+j)//2+1,j)
        if card[result1] == card[result2]:     #카드가 서로 같으면
            return result1
        else:                                  #카드가 다르면
            if card[result1]==1 and card[result2]==2:
                return result2
            elif card[result1]==1 and card[result2]==3:
                return result1
            elif card[result1]==2 and card[result2]==1:
                return result1
            elif card[result1]==2 and card[result2]==3:
                return result2
            elif card[result1]==3 and card[result2]==2:
                return result1
            elif card[result1]==3 and card[result2]==1:
                return result2

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    card = list(map(int,input().split()))
    print('#{} {}'.format(tc,find(0,N-1)+1))