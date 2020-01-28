# i = 0
# while i<74:
#     i += 1
#     if str(i)[-1] == '3':
#         print(i, end=" ")
#     else:
#         continue

sum1=0
sum2=0
a = list(map(int, input().split()))
for i in range(len(a)//2):
    sum1 += a[2*i+1]
for k in range(len(a)//2):
    sum2 += a[2*k]
avg = sum2/(len(a)//2)

print('sum : {}'.format(sum1))
print('avg : {}'.format(avg,'.1f'))