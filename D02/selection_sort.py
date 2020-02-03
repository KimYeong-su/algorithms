'''
선택 정렬 -> 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

'''

def selectionSort(a):
    for i in range(0,len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j     # 탐색 구간내의 최소값의 인덱스 찾기
        a[i], a[min] = a[min], a[i]  # 탐색구간의 가장 앞이랑 최소값을ㄴ바꿈
    return a

arr = [5,3,2,1,4]
print(selectionSort(arr))