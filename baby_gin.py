#반복문을 이용해서 순열을 구현해보세요
#1,2,3
#  완전탐색(단점 : 선택해야하는 숫자가 늘어나면 시간복잡도가 기하급수적으로 커짐)
# for i1 in range(1,4):
#     for i2 in range(1,4):
#         if i1 != i2:
#             for i3 in range(1,4):
#                 if i3 != i2 and i3 != i1:
#                     print(i1, i2, i3)

initial = [3, 2, 5, 4, 1]
def bubble_sort(initial_list):                          #내가 짠거
    num = len(initial_list)
    while num > 0:
        for i in range(0,num-1):
            if initial_list[i] > initial_list[i+1]:
                temp = initial_list[i]
                initial_list[i] = initial_list[i+1]
                initial_list[i+1] = temp
        num -= 1
    return initial_list
#print(bubble_sort(initial))

def Bubble_sort(a):                                     #강사님이 짠거
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
#print(Bubble_sort(initial))

arr = [0, 4, 1, 3, 1, 2, 4, 1]
def Counting_sort(a): #내가 푼거
    counts = [0, 0, 0, 0, 0]
    for i in arr:
        counts[i] += 1

    for i in range(len(counts)-1):
        counts[i+1] = counts[i]+counts[i+1]

    temp = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(len(arr)-1,0,-1):
        temp[(counts[arr[j]])-1] = arr[j]
        counts[arr[j]] -=1
    return temp
print(Counting_sort(arr))

# def counting_sort(A,k): #A : 정렬할 배열 k : 배열의 최대값
#     c = [0 * k]
#     for i in range(0, len(A)):
#         c[A[i]] += 1
#
#     for j in range(len(c)-1):
#         c[j+1] += c[j]



