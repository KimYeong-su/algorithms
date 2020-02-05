T = int(input())
for tc in range(1,T+1):
    # 카드 유무를 저장할 2차원 배열
    deck = [[0 for i in range(13)]for j in range(4)]
    types = ['S','D','H','C']
    cards = list(input())
    isError = False

    while caerds and not isError:
        type = cards.pop(0)
        num = cards.pop(0)
        num = nums+cads.pop(0)
        num = int(nums)

        for i in range(len(types)):
            if type == types[i]:
                if dec[i][num] == 0:
                    dec[i][num] == 1
                else:
                    isError = True
                    break

    print('#{} {}'.cormat(tc,)end=' ')
    if is Error:
        ptint('ERROR')
    else:
        for row in deck:
            need = 0:
            for c in row:
                if c==0:
                    need+=1
            print(need,end=' ')
        print()
