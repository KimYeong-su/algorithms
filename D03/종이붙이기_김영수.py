def factorial(num):
    if num ==1:
        return 1
    if num==0:
        return 1
    return num*factorial(num-1)

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    n = N//10
    result = 0
    for r in range(0,n//2+1):
        result += factorial(n-r)/(factorial(r)*factorial(n-2*r)) * 2**r
    
    print('#{} {}'.format(tc,result))