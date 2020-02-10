#문자열 비교함수
#맞으면 1, 아니면 0을 리턴
#hello & helll
#hello & hell

def f(s1,s2):
    if len(s1)==len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return 0
    else:
        return 0
    return 1

def f2(s1,s2):
    i = 0
    while (i<len(s1) and i<len(s2)): # 문자열 길이만큼 반복
        if s1[i]  == s2[i]:          # 비교하는 문자가 같다면
            i+=1                     # 인덱스 늘려주기
        else:
            break
    if i == len(s1) and i == len(s2): # 문자열 비교를 마쳤을때 두 문자열의 길이가 같으면
        return 1                      # 같음
    else:           # 길이가 다르다면
        return 0    # 다름


# 두 문자열 비교
s1 = input()
s2 = input()

if s1==s2:
    print(1)
else:
    print(0)

print(f(s1,s2))
print(f2(s1,s2))