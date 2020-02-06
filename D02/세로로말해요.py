'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''
T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    # 열 방향으로 읽어 오기
    # 0행 0열 -> 1행 0열 -> 2행 0열 ...
    # 0행 1열 -> 1행 1열 -> 2행 1열 ...
    for i in range(15):
        for j in range(5):
            # 접근하려는 열이 접근 가능한지 확인
            if i < len(arr[j]) and j < len(arr):
                print(arr[j][i], end=' ')
    print()