cases = int(input())

for case in range(cases):
    K, N, M = map(int,input().split()) # k는 최대 이동가능 정류장, N 최종목적지, M 충전기 횟수
    c = [0]*(N+1) # 리스트 만들기(0~11)

    for i in map(int, input().split()): # 정류장이 있으면 1로 처리
        c[i] = 1

    cnt = 0 #충전을 하고 가는 횟수
    a = 0 # 현재 위치

    while a < N: # 도착하지 않았으면 반복
        i = K # 최대로 갈 수 있는 구간을 주소가 업데이트 될때 마다 초기화
        while i>0: #한번 충전을 하고 갈 수 있는 동안 확인
            if a+i<N: #현재 위치가 아직 도착지점 보다 뒤에 있으면
                if c[a+i] == 1: #그리고 정류소가 있으면
                    cnt += 1 #들린 횟수 증가
                    a += i #현재위치 업데이트
                    i = 0 #반복문 탈출
                else:
                    if i==1: # 그 구간에 정류소가 없으면
                        i = 0 #반복문 탈출
                        a = N
                    else: # 구간안에서 반복
                        i -= 1
            else: #도착 하면
                i = 0 # 반복문 탈출
                a = N+1


    if a > N: #도착지점에 도착하면
        print('#{} {}'.format(case + 1, cnt))
    else: #도착 지점에 도달 못하면
        print('#{} 0'.format(case + 1))