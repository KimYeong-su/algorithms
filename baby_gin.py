# #반복문을 이용해서 순열을 구현해보세요
# #1,2,3
# #  완전탐색(단점 : 선택해야하는 숫자가 늘어나면 시간복잡도가 기하급수적으로 커짐)
# # for i1 in range(1,4):
# #     for i2 in range(1,4):
# #         if i1 != i2:
# #             for i3 in range(1,4):
# #                 if i3 != i2 and i3 != i1:
# #                     print(i1, i2, i3)
#
# initial = [3, 2, 5, 4, 1]
# def bubble_sort(initial_list):                          #내가 짠거
#     num = len(initial_list)
#     while num > 0:
#         for i in range(0,num-1):
#             if initial_list[i] > initial_list[i+1]:
#                 temp = initial_list[i]
#                 initial_list[i] = initial_list[i+1]
#                 initial_list[i+1] = temp
#         num -= 1
#     return initial_list
# #print(bubble_sort(initial))
#
# def Bubble_sort(a):                                     #강사님이 짠거
#     for i in range(len(a)-1,0,-1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
# #print(Bubble_sort(initial))
#
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# def Counting_sort(a): #내가 푼거
#     counts = [0, 0, 0, 0, 0]
#     for i in arr:
#         counts[i] += 1
#
#     for i in range(len(counts)-1):
#         counts[i+1] = counts[i]+counts[i+1]
#
#     temp = [0, 0, 0, 0, 0, 0, 0, 0]
#     for j in range(len(arr)-1,0,-1):
#         temp[(counts[arr[j]])-1] = arr[j]
#         counts[arr[j]] -=1
#     return temp
# #print(Counting_sort(arr))
#
# def counting_sort(A,B,k): #A : 정렬할 배열 k : 배열의 최대값
#     c = [0]*k
#     for i in range(0, len(A)):
#         c[A[i]] += 1
#
#     # 카운트 배열 조작하기 : 숫자들이 들어갈 자리를 표현하도록 내 앞 인덱스 숫자를 더해서 대입
#     for i in range(1,len(c)):
#         c[i] += c[i-1]
#
#     # 정렬하기
#     for i in range(len(A)-1,0,-1):
#         c[A[i]] -= 1
#         B[c[A[i]]] = A[i]
#
#     return B
# print(counting_sort(arr,[0]*len(arr),5))
#
#
#
cases = int(input())
for case in range(cases):
    num = int(input())
    c = [0]*10
    for i in str(num):
        c[int(i)] += 1
    for j in range(len(c)):
        if c[j] > 3:
            c[j] -= (c[j]//3)*3

    for k in range(len(c)-2):
        while c[k] > 0:
            if c[k]>0 and c[k+1]>0 and c[k+2]>0:
                c[k] -= 1
                c[k+1] -= 1
                c[k+2] -= 1
            else:
                break

    if c == [0]*10:
        print('#{} baby_gin'.format(case+1))
    else:
        print('#{} fail'.format(case+1))