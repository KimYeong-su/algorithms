T = int(input())

for tc in range(1,T+1):
    n = int(input())
    bolt = list(map(int, input().split()))
    bolts = []  # 빈 리스트 생성
    for i in range(0,2*n,2):
        bolts.append(bolt[i:i+2])

    temp = []   #나사 연결용 리스트
    temp.append(bolts.pop(0))   # temp의 첫번째 나사 넣기
    cnt = 0
    while cnt < n:
        for j in range(len(bolts)):
            if temp[-1][1] == bolts[j][0]:
                temp.append(bolts[j])
            elif temp[0][0] == bolts[j][1]:
                temp.insert(0,bolts[j])
        cnt += 1
    ans = ''
    for x, y in temp:
        ans += ' ' + str(x) + ' ' + str(y)

    print('#{} {}'.format(tc,ans))