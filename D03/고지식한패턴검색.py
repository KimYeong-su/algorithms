p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)

def BruteForce(p,t):
    i = 0
    j = 0
    while j < M and i < N :     # 패턴의 길이, 전체 텍스트 길이만큼 반복
        if t[i] != p[j]:        # 맞지 않는다면
            i = i - j           # 시작점 한칸 옮기기
            j = -1              # 나중에 +1을 하므로 -1에서 시작
        i = i + 1               # 옆칸 검사 
        j = j + 1
    if j == M: return i - M
    else: return -1