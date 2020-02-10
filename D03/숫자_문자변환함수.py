str_num = '123'
print(str_num)
print(type(str_num))        # type() : 타입확인함수
num = int(str_num)                # int() : 타입변환함수 : str -> int
print(num)
print(type(num))

# 실수 변환
print('3.14')
print(type('3.14'))
print(float('3.14'))
print(type(float('3.14')))

#수를 문자로
print(str(123))     #str() : 문자열로
print(type(str(123)))

#ASCII code 탐색
print(ord('a')) #'a'->97
print(ord('0')) #'0'->48

def atoi(s):
    result = 0
    for i in s:
        result = result*10
        result += int(i)
    return result

def atoi2(s):
    result = 0
    for i in s:
        result = result*10
        result += ord(i)-48
    return result

#숫자로 생긴 문자 -> 숫자로 변경하는 함수
s = input()
r = atoi(s)     #문자를 입력받아서 int형으로 변환해서 리턴
r2 = atoi2(s)
print(r)
print(type(r))
print(r2)
print(type(r2))