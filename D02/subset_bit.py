# # <<연산자 : 피연산자의 피트열을 왼쪽으로 디동시킴
# # 1<<n : 원소가 n인 경우 n만큼 이동
#
# # print(1<<1)
# # print(1<<2)
# # print(1<<3)
#
# # &연산자 : 비트연산자 1010  0111
# print(10&7) # 0010 -> 2
#
# # 10을 이진수로 -> 10은 16보다 작고 8보다 작음 -> 2^4는 안되고 2^3은 포함가능
# print(bin(10))
#
# # 7을 이진수로
# print(bin(7))


arr = [-7, -3, -2, 5, 8]
n = 5
ans = False
for i in range(1<<n):#1<<3 : 8(1000) => range(8)
    sum = 0
    for j in range(n):
        if i&(1<<j):
            sum += arr[j]
    if sum == 0:
        ans = True

print(ans)

