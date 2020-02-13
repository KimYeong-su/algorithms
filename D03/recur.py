#재귀함수
#자기자신을 호출하는 함수
'''
#재귀함수의 구조
기본 파트 : base case
    적어도 하나의 recursion에 빠지지 않는 경우가 존재해야 함
유도 파트 : recursive case
    recursion을 반복하다보면 결국 base case로 수렴해야 함

'''
# def func(k):
#     if k < 0: # base 파트
#         return
#     print('hello')
#     func(k-1)
#
# func(5)


#재귀함수를 이용해서 1~10까지의 합을 구하세요
def add(K,result):
    if K < 0:
        print(result)
        return
    else:
        add(K-1,result+K)

add(10,0)

def add2(k):
    if k == 0:
        return 0
    else:
        return k + add2(k-1)

print(add2(10))

#정해진 횟수만큼 호출하기
#호출횟수에 대한 정보를 인자로 전달
#정해진횟수에 다다르면 재귀호출 중단
#case에 맞게 짜자.. -> 주어진 조건에 맞는 재귀함수를 짜야함(이 case같은 경우는 0부터 몇 개까지 출력이 가능한지 찾는 문제)
# 조건 자체가 0부터 시작이고 몇개 출력인지가 문제임!
def f(n,k):
    if k==0:
        return
    print(n)
    f(n+1,k-1)

f(0,5) #n : 변하는 숫자, k : 지정한 횟수

'''
원하는 조건을 찾으면 중단하는 경우
주어진 집합에 v가 있으면 1, 없으면 0을 리턴하는 재귀함수
'''

a = [3,7,6,2,1,4,8,5]
v = 2
def find(i,n,v):
    if i >= n:
        print(0)
        return
    if a[i]==v:
        print(1)
        return
    find(i+1,n,v)

find(0,len(a),v)

'''
팩토리얼
3! = 3 * 2 * 1

f(n) = n * f(n-1)
'''

def factorial(n):
    if n==1:
        return 1
    return factorial(n-1)*n

print(factorial(3))

def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(5))

# 메모이제이션(memoization) : 연산결과를 저장 -> 중복계산을 안함
# 메모를 저장하기위한 배열을 할당하고 0으로 초기화

def fibo1(n):
    # n이 2보다 길거나 크고 n이 메모 길이보다 길면 -> 아직 계산되지 않았다면
    if n >=2 and len(memo) <= n:
        memo.append(fibo1(n-1)+fibo1(n-2))   # 계산을 하고 메모이제이션 배열에 저장
    return memo[n] #아니라면 -> 이미 계산된 값이면 -> 메모이제이션 배열에 저장된 값을 리턴

memo=[0,1]  #메모이제이션 초기화
print(fibo1(5))

# DP  적용
def fibo2(n):
    f = [0,1]
    for i in range(2,n+1):  # n[2]->m0
        f.append(f[i-1]+f[i-2])
    return f[n]
print(fibo2(5))